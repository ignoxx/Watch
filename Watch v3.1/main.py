#! /usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import subprocess
import urllib2
import time
import json
import bs4
import sys
import re
import os

# Design file
from src.gui import design

VERSION = "3.1.0"

# URL Template http://bs.to/serie/SERIENAME/EPISODE/PART-TITLE
BASE_URL_SERIES = 'http://bs.to/andere-serien'
BASE_URL = 'http://bs.to'


class WatchApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super(WatchApp, self).__init__(parent)
        self.setupUi(self)

        self._log("Watch v%s by IGnoXX"%(VERSION))

        # reload all icons
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/gui/add.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBtn.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/gui/reload.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reloadBtn.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/gui/remove.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeBtn.setIcon(icon)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./src/gui/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # events
        self.addBtn.clicked.connect(self._addSerie)
        self.removeBtn.clicked.connect(self._removeSerie)
        self.userInput.returnPressed.connect(self._addSerie)
        self.watchBtn.clicked.connect(self._watchSerie)
        self.reloadBtn.clicked.connect(self._reloadSerie)

        # check if 'serie-file' exists
        if not os.path.isfile("./src/tmp/serie.watch"):
            self._log("Reload files to grab information faster")
        
        # load savefile
        self.sav_file = self.savefile()

        for serie in self.sav_file:
            self.serieList.addItem(serie)
        
        if len(self.sav_file) == 0:
            self._log("No saved series found")
        else:
            self._log("All series loaded")
        
    
    def format_name(self, name): # maybe just encode/decode string?
        format = [(" ", "-"), ("(", ""), (")", ""), (",", ""), (u"í", "i"), (u"ó", "-"), (u"’",""), ("'", "")]
        
        for f in format:
            name = name.replace(f[0], f[1])
        
        return name


    def savefile(self, action = "load"):
        if action == "load":
            if os.path.isfile("./src/tmp/user.sav"):
                try:
                    with open("./src/tmp/user.sav", "rb") as f:
                        return json.loads( f.read() )
                except:
                    return {}
            else:
                return {}

        elif action == "save":
            try:
                with open("./src/tmp/user.sav", "w") as f:
                    f.write(json.dumps(self.sav_file))
                    return True

            except:
                return False

    def get_serie_file(self): # Download page
        html = urllib2.urlopen(BASE_URL_SERIES).read()
        with open("./src/tmp/serie.watch", "wb") as f:
            f.write(html)

    def _reloadSerie(self):
        self.get_serie_file()
        self._log("Loading files..Done")

    def findWholeWord(self, w):
        return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
    

    def _removeSerie(self):
        userSelection = self.get_list_selection()

        # Check if user did any selection
        if not userSelection:
            self._log("No serie selected")
            return
        
        if userSelection in self.sav_file:
            del self.sav_file[userSelection]
            self._log("`%s` removed"%userSelection)
        else:
            self._log("`%s` can't be removed"%userSelection)
        
        # save changes
        self.savefile("save")

        self.serieList.clear()
        for serie in self.sav_file:
            self.serieList.addItem(serie)
    
    def _addSerie(self):
        # grab users input
        userInput = str(self.userInput.text())

        # check if serie is not an empty string
        if not userInput:
            self._log("Invalid input")
            return

        # Check if serie does not exist already
        for i in range(self.serieList.count()):
            if userInput.lower() == str(self.serieList.item(i).text()).lower():
                self._log("`%s` already added"%(userInput.title()))
                return
        
        # check if serie exists in bs.to DB
        if os.path.isfile("./src/tmp/serie.watch"):
            with open("./src/tmp/serie.watch", "rb") as f:
                bsDB = f.read()
        else:
            bsDB = urllib2.urlopen(BASE_URL_SERIES).read()
        
        
        if self.findWholeWord(userInput)(bsDB) == None:
            self._log("`%s` not found"%userInput)
            return
        
        # grab serie information like, episodes, link etc..
        userInputFormated = self.format_name(userInput)
        season = 1
        episode = 1
        
        season_url = BASE_URL + '/serie/%s/%s'%(userInputFormated, season)

        # Grab all Episode names from season 1 and generate url
        episodeNames = {}
        episodeNames[str(season)] = self.findEpisodeNames(season_url)

        # if episodeNames is empty, it means the serie was not found
        if not len(episodeNames):
            self._log("`%s` not found"%userInput)
            return
        
        # generate URL
        episode_url = BASE_URL + '/serie/%s/%s/%s-%s'%(userInputFormated, season, episode, episodeNames[str(season)][0])

        # Grab the max seasons
        max_seasons = len(re.findall('<li><a href="serie/.*?/\d+">.*?</a></li>', str(urllib2.urlopen(episode_url).read())))

        # count max episodes per serie
        episodes = {}
        for season in range(1, max_seasons+1):
            episode_url = BASE_URL + '/serie/%s/%s'%(userInputFormated, season)
            
            episodeNames[str(season)] = self.findEpisodeNames(episode_url)
            episodes[str(season)] = len(episodeNames[str(season)])
        

        # save new serie in DB and add it to the list
        userInput = userInput.title()
        self.sav_file[userInput] = {
            "max_seasons":      max_seasons,
            "overview":         episodes,
            "current_season":   1,
            "current_episode":  0,
            "url":              season_url,
            "episodeNames":     episodeNames
        }
        
        # save
        self.savefile("save")

        self.serieList.addItem(userInput)

        self._log("`%s` successfully added"%userInput)
        self.userInput.clear()

    
    def findEpisodeNames(self, url):
        episode_name_list = []
        html = urllib2.urlopen(url).read()
        html = html.splitlines()
        for line in html:
            matches = re.findall('<span lang="en">.*?</span>', line)
            for match in matches:
                episode_name_list.append( self.format_name(bs4.BeautifulSoup(match, 'html.parser').string) )

        return episode_name_list

    def internet_on(self):
        try:
            for timeout in [1,5,10,15]:
                try:
                    response=urllib2.urlopen('http://google.de',timeout=timeout)
                    return True
                except urllib2.URLError as err: pass
            return False
        except:
            return None


    def _watchSerie(self):
        userSelection = self.get_list_selection()

        if not self.internet_on():
            self._log("Internet..error")
            return


        # Check if user did any selection
        if not userSelection:
            self._log("No serie selected")
            return
        
        # load serie data
        serieData = self.sav_file[userSelection]

        # increment season/episode 
        current_season = serieData["current_season"]
        current_episode = serieData["current_episode"]

        if current_episode < serieData["overview"][str(current_season)]:
            current_episode += 1
        else:
            if current_season < int(max(serieData["overview"])):
                current_season += 1
                current_episode = 1
            else:
                self._log("")
                self._log("Serie `%s` has no new episodes/seasons anymore."%(userSelection))
                self._log("In case new episodes/seasons are released, reload files!")
                return

        # open serie
        serieNameFormated = self.format_name(userSelection)
        next_episode_url = BASE_URL + '/serie/%s/%s'%(serieNameFormated, current_season)
        next_episode_name = "Watch-v3-ignoxx-at-yahoo-dot-de"#doesent matter, one letter is enough #serieData["episodeNames"][str(current_season)][current_episode-1] #self.findEpisodeNames(next_episode_url)

        full_episode_url = BASE_URL + '/serie/%s/%s/%s-%s'%(serieNameFormated, current_season, current_episode, next_episode_name)
        
        # update serie data
        serieData["current_season"] = current_season
        serieData["current_episode"] = current_episode

        self.sav_file[userSelection] = serieData
        self.savefile("save")

        # finishing..
        self._log("---------------------")
        self._log("Redirecting..%s"%(full_episode_url))
        self.open_url(full_episode_url)

    def _log(self, text):
        self.logBrowser.append("%s"%text)
        

    
    def get_list_selection(self):
        try:
            return str(self.serieList.currentItem().text())
        except:
            return False
    
    def open_url(self, path):
        if os.name == "nt": # Windows
            os.startfile(path)
            
        elif sys.platform == "darwin": # Mac
            subprocess.call(['open', path])
            
        else: # Linux
            subprocess.call(['xdg-open', path])



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = WatchApp()
    form.show()
    app.exec_()
