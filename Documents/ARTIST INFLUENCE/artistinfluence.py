#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from termcolor import colored, cprint
import sys, time, os, subprocess, random, base64, codecs, requests, re, json, ssl, datetime, gc, threading, ctypes
from requests.auth import HTTPProxyAuth
os.system('color')
import websocket, spotipy, socket
import spotipy.util as util
from threading import Thread
from multiprocessing import Process, Queue, Value
import multiprocessing
from os import listdir
import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
mysql.connector.pooling.CNX_POOL_MAXSIZE = 15000
import argparse
from urllib3 import ProxyManager, make_headers
import certifi
from io import BytesIO   
import urllib3
import pycurl
from urllib.parse import urlencode
from urllib import request, parse
urllib3.disable_warnings()
from licensing.models import *
from licensing.methods import Key, Helpers
threading.stack_size(256000)

def pleaserunfortwohours(new,useprox,t_chunk,i,q, autos, nautos, autof, nautof, ipmode, ipconf, plid, tpos, stop, follows, savess, realsent, round,nr,plen1,plen2,oout,percentage,rtime,authstr):
    connection_pool = 1
    connect_db_host = "191.101.192.57"
    try:
        connect_db_file = open("host.txt","r")
        connect_db_host = connect_db_file.readline().rstrip()
        connect_db_file.close()
    except:
        #cprint("can not find host.txt, trying to connect to good ol' mama africa..","yellow")
        connect_db_host = "191.101.192.57"
    try:
        connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="py_pool"+str(i), pool_size=int(100), pool_reset_session=True, host=str(connect_db_host), database='boombox', user='admin', password='boombox', autocommit=True)
    except:
        cprint("mysqlerror, can not connect to db on "+connect_db_host,"red")
        os._exit(0)
    def killAll():
        tenum = threading.enumerate()
        for ot in tenum:
            if( ot.name != 'MainThread'):
                if( ot.name != 'writer'):
                    if( ot.name != 'spm'):
                        if(not 'killa' in ot.name):
                            if(not 'checker' in ot.name):
                               terminate_thread(ot)
        return True
    def terminate_thread(thread):
        if not thread.isAlive():
            return
    
        exc = ctypes.py_object(SystemExit)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(thread.ident), exc)
        if res == 0:
            raise ValueError("nonexistent thread id")
        elif res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    class hackify(object):
        def __init__(self, atkn, proxy, authstr, mynr, myname, q, connection_pool, auto, nautos, autof, nautof, ipmode, ipconf, plid, tpos, stop, useprox, follows, savess, realsent, oout, percentage):
            Thread.__init__(self)
            self.mynr = mynr
            self.token = atkn.replace(" ","")
            self.proxy = proxy
            self.proxyuser = authstr.split(':')[0]
            self.proxypass = authstr.split(':')[1]
            self.name = myname
            self.msg = "first"
            self.que = q
            self.oout = str(oout)
            self.connection_obj = 1
            self.connection_pool = connection_pool
            self.account = "duMMBoi_1337@hotmail.com:rusty2007" ###### why a hard coded value for email
            self.device_id = str('%032x' % random.getrandbits(128))
            self.device_type = random.choice(['smartphone','smartphone','computer'])
            self.device_name = ''
            self.dev_platf = ''
            self.dev_seq = '1'
            self.file_id = ''
            self.dev_os = ''
            self.percentage = percentage
            self.keyy = ''
            self.sp = ''
            self.cp = False
            self.lid = 0
            self.mid = '1'
            self.seq_id = 0
            self.autos = autos
            self.nautos = nautos
            self.autof = autof
            self.nautof = nautof
            self.ipmode = ipmode
            self.ipconf = ipconf
            self.useprox = useprox
            self.step = 1
            self.plid = plid
            self.tpos = tpos
            self.sstop = stop
            self.follows = follows
            self.savess = savess
            self.realsent = realsent
            self.var50k, self.tplay, self.n_plays, self.sto, self.ti = 0,0,0,0,0
            self.n_streams = 0
            self.savedinlib = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
            self.libids = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
            if(self.device_type == 'smartphone'):
                names = ["Olivia","Amelia","Isla","Emily","Ava","Mia","Sophia","Isabella","Grace","Ella","Evie","Charlotte","Jessica","Daisy","Sophie","Francesca","Alicia","Sienna","Ivy","Isabelle","Evelyn","Chloe","Millie","Matilda","Scarlett","Eva","Lucy","Sofia","Lola","Bella","Ellie","Thea","Lilly","Bella","Molly","Holly","Amber","Emma","Hannah","Violet","Georgia","Nancy","Jasmine","Anna","Lea","Victoria","Darcey","Laura","Annabelle","Melanie","Vanessa","Melody","Amelie","Emelie","Maria","Clara","Madison","Megan","Maci","Felicity","Joy","Kenzie","Veronica","Margot","Addilyn","Lana","Cassidy","Ryan","Keira","Harlow","Miranda","Angel","Amanda","Daniella","Royalty","Gwendolyn","Ophelia","Heaven","Jordan","Madeleine","Esmeralda","Kira","Miracle","Elle","Amari","Danielle","Daphne","Willa","Haley","Gia","Kaitlyn","Oakley","Kailani","Winter","Alicia","Serena","Nadia","Aviana","Demi","Jada","Braelynn","Dylan","Ainsley","Alison","Camryn","Avianna","Bianca","Skyler","Scarlet","Maddison","Nylah","Sarai","Regina","Dahlia","Nayeli","Raven","Helen","Adrianna","Averie","Skye","Kelsey","Tatum","Kensley","Maliyah","Erin","Viviana","Jenna","Anaya","Carolina","Shelby","Sabrina","Mikayla","Annalise","Octavia","Lennon","Blair","Carmen","Yaretzi","Kennedi","Mabel","Zariah","Kyla","Christina","Selah","Celeste","Eve","Mckinley","Milani","Frances","Jimena","Kylee","Leighton","Katie","Aitana","Kayleigh","Sierra","Kathryn","Rosemary","Jolene","Alondra","Elisa","Helena","Charleigh","Hallie","Lainey","Avah","Jazlyn","Kamryn","Mira","Cheyenne","Francesca","Antonella","Wren","Chelsea","Amber","Emory","Lorelei","Nia","Abby","April","Emelia","Carter","Aylin","Cataleya","Bethany","Marlee","Carly","Kaylani","Emely","Liana","Madelynn","Cadence","Matilda","Sylvia","Myra","Fernanda","Oaklyn","Elianna","Hattie","Dayana","Kendra","Maisie","Malaysia","Kara","Katelyn","Maia","Celine","Cameron","Renata","Jayleen","Charli","Emmalyn","Holly","Azalea","Leona","Alejandra","Bristol","Collins","Imani","Meadow","Alexia","Edith","Kaydence","Leslie","Lilith","Kora","Aisha","Meredith","Danna","Wynter","Emberly","Julieta","Michaela","Alayah","Jemma","Reign","Colette","Kaliyah","Elliott","Johanna","Remy","Sutton","Emmy","Virginia","Briana","Oaklynn","Adelina","Everlee","Megan","Angelica","Justice","Mariam","Macie","Karsyn","Alanna","Aleah","Mae","Mallora","Esme","Skyla","Madilynn","Charley","Allyson","Hanna","Shiloh","Henley","Macy","Maryam","Ivanna","Ashlynn","Lorelai","Amora","Ashlyn","Sasha","Baylee","Beatrice","Itzel","Priscilla","Marie","Jayda","Liberty","Rory","Alessia","Alaia","Janelle","Kalani","Gloria","Sloan","Dorothy","Greta","Julie","Zahra","Savanna","Annabella","Poppy","Amalia","Zaylee","Cecelia","Coraline","Kimber","Emmie","Anne","Karina","Kassidy","Kynlee","Monroe","Anahi","Jaliyah","Jazmin","Maren","Monica","Siena","Marilyn","Reyna","Kyra","Lilian","Jamie","Melany","Alaya","Ariya","Kelly","Rosie","Adley","Dream","Jaylah","Laurel","Jazmine","Mina","Karla","Bailee","Aubrie","Katalina","Melina","Harlee","Elliot","Hayley","Elaine","Karen","Dallas","Lylah","Ivory","Chaya","Rosa","Aleena","Braelyn","Nola","Alma","Leyla","Pearl","Addyson","Roselyn","Lacey","Lennox","Reina","Aurelia","Noa","Janiyah","Jessie","Madisyn","Saige","Alia","Tiana","Astrid","Cassandra","Kyleigh","Romina","Stevie","Haylee","Zelda","Lillie","Aileen","Brylee","Eileen","Yara","Ensley","Lauryn","Giuliana","Livia","Anya","Mikaela","Palmer","Lyra","Mara","Marina","Kailey","Liv","Clementine","Kenna","Briar","Emerie","Galilea","Tiffany","Bonnie","Elyse","Cynthia","Kinslee","Tatiana","Joelle","Armani","Jolie","Nalani","Rayna","Yareli","Meghan","Rebekah","Addilynn","Faye","Zariyah","Lea","Aliza","Julissa","Lilyana","Anika","Kairi","Aniya","Noemi","Angie","Crystal","Bridget","Ari","Davina","Amelie","Amirah","Annika","Elora","Xiomara","Linda","Hana","Laney","Mercy"]
                self.device_name = str(random.choice(names))+"'s Iphone"
                self.dev_os = 'ios'
                self.dev_platf = 'ios_sdk_v1'
            else:
                self.device_name = random.choice(["Bose Soundbar 700","Web Player (Chrome)","WIN-9DVAMKIGFGF","WIN-2DFAMKIGFGL","WIN-9DVAMKIGFGA","WIN-9DVAMKIGFGB","Web Player (Firefox)","WIN-9DVAMKIGFGC","WIN-9DVAMKIGFGD","WIN-9DVAFCIGFGE","WIN-9DVAMKIGFGF","WIN-9DVAMKIGFGH","WIN-5GDAMKIGFGI","WIN-9BVAMEIGFGJ","WIN-9DVEMKIGFGK","WIN-9OAFMKIGFGM","WIN-1A3KIGFGN","WIN-3LOAMKIGFGO","WIN-6YMAMKIGFGP","WIN-SDVAMKIGFGQ","WIN-9OKMKIGFGR","WIN-1AVAMKIGFGS","WIN-7DVABKIGFGT","WIN-8GVAMKIGFGU","WIN-4GVAMKIGFGV","WIN-8FVAMKIGFGW","WIN-4DFAMKIGFGX","WIN-9DVAMVIGFGY","WIN-3DVAMKIGFGZ"])
                self.dev_os = 'windows'
                self.dev_platf = random.choice(['chrome','gecko'])
        def on_message(ws, message):
            cur=1
            try:
                import time
                import threading.Thread
            except:
                ok = 1
    
            def raise_exception(ws): 
                thread_id = ws.get_id() 
                res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit)) 
                if res > 1: 
                    ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
    
            def getCount(self, tplay, name):
                import time
                sql = "SELECT counter."+str(tplay)+" FROM counter WHERE counter.name="+str(name) 
                ########
                # To get the amount of plays that a track has
                ########
                failed=True
                count = 1 # count of how many times a track has been played
                while(failed): 
                    ########
                    # what is this section for?
                    ########
                    try:
                        connection_obj = self.connection_pool.get_connection()
                        cur = connection_obj.cursor()
                        cur.execute(sql)
                        myresult = cur.fetchone()
                        count = int(myresult[0])
                        connection_obj.close()
                        failed=False
                    except Exception as e:
                        time.sleep(random.randint(1,2))
                return count
    
            def writeCount(ws, name):
                import threading, time, gc
                failed=0
                while(failed<3):
                    try:
                        ws.connection_obj = ws.connection_pool.get_connection()
                        cur = ws.connection_obj.cursor()
                        cur.execute("UPDATE orders SET did24=did24+1 WHERE id="+str(name))
                        cur.execute("UPDATE orders SET did_total=did_total+1 WHERE id="+str(name))
                        ws.connection_obj.close()
                        failed=5  
                    except Exception as e: 
                        cprint(e,'red')
                        gc.collect()
                        failed=failed+1
                        time.sleep(random.randint(1,3))
                return True
    
            def createDevice(ws, access_token, keyy, nautof, nautos): ##### adds device to new account user
                conni = False
                tried = 0
                proxies = { "https" : "http://"+str(ws.proxy) }
                auth = HTTPProxyAuth(ws.proxyuser, ws.proxypass) 
                ########
                # attaching proxy settings of currently logged in user
                ########
                failed = True
                ttt = 0
                if failed:
                    sp=1
                    #proxx = { "https" : "http://"+ws.proxyuser+":"+ws.proxypass+"@"+str(ws.proxy) }
                    sp = spotipy.Spotify(auth=access_token,proxies=proxies)
                    ########
                    # TYPO?????? "SPOTIPY"
                    ########
                    sp.trace_out = False
                    #curp = sp.currently_playing()
                    #if curp != None:
                    #    cprint('acc already playing..aborting thread','yellow')
                    #    return
                    #else:
                    #    print("got1")
                failed = False
               
                while(conni == False):
                    tried = tried+1
                    if(tried == 2):
                        return 1
                    try:
                        bearer = str("Bearer "+access_token)
                        postData = ("""{"device":{"device_id":"DEVID","device_type":"DEVTYPE","brand":"public_js-sdk","model":"harmony-DEVPLAT."""+str(random.randint(49,76))+"""-DEVOS","name":"DEVNAME","metadata":{},"capabilities":{"change_volume":true,"audio_podcasts":true,"enable_play_token":true,"play_token_lost_behavior":"pause","disable_connect":false,"manifest_formats":["file_urls_mp3","file_urls_external","file_ids_mp4","file_ids_mp4_dual"]}},"connection_id":\""""+str(keyy+"=")+"""\","client_version":"harmony:3.19.1-441cc8f","previous_session_state":null,"volume":65535}""").replace("DEVID",ws.device_id).replace("DEVOS",ws.dev_os).replace("DEVPLAT",ws.dev_platf).replace("DEVTYPE",ws.device_type).replace("DEVNAME",ws.device_name).replace("-windows",ws.dev_os).replace("-chrome",ws.dev_platf)
                        headers = { 'Authorization' : bearer, 'Content-Type' : 'application/json' }
                        p=1
                        p = requests.post("https://gew-spclient.spotify.com/track-playback/v1/devices", data=postData , headers=headers, proxies=proxies)#, auth=auth)
                        
                        ws.dev_seq = 0
                        ws.dev_seq = int(str(re.search('initial_seq_num":(.*),"device_keep_alive_update_seconds', str(p.content)).group(1)))
                        conni=True
                        #cprint('device created ahuh','cyan')
                        #print(ws.dev_seq)
                    except Exception as e:
                        #cprint(e,"red")
                        time.sleep(1)

                return access_token, sp, ws.dev_seq

            def cashify_play(ws, message, access_token, dev_seq, step, dev_os, dev_platf, seq_id, autof, nautof, autos, nautos, device_id, tplay, var50k, proxy, sp, device_name,useprox,ti,savess,follows,realsent): 
                ######### point of this function is to run a single play - or multiple plays??? infinite??
                failed = 0
                proxies = ""
                auth = ""
                while(failed<3):
                    try:
                        import time
                        proxies = { "https" : "http://"+str(ws.proxy) }
                        if(failed == 1):
                            nprx = str(ws.proxy).split(':')[0]+':'+str(int(str(ws.proxy).split(':')[1])+1)
                            proxies = { "https" : "http://"+str(nprx) }
                        if(failed == 2):
                            nprx = str(ws.proxy).split(':')[0]+':'+str(int(str(ws.proxy).split(':')[1])+1)
                            proxies = { "https" : "http://"+str(nprx) }     
                        auth = HTTPProxyAuth(ws.proxyuser, ws.proxypass)
                        p=1
                        ws.ws.send('{"type":"ping"}')
                        bearer = "Bearer "+access_token
                        conurl = "https://api.spotify.com/v1/track-playback/v1/devices/"+device_id+"/state"
                        headers = {'Access-Control-Request' : 'authorization'}
                        p = requests.options(conurl , headers=headers,proxies=proxies)#, auth=auth)
                        conurl = "https://api.spotify.com/v1/me/feature-flags?tests=tps_send_all_state_updates"
                        headers = {'Access-Control-Request' : 'authorization'}
                        p = requests.options(conurl , headers=headers, proxies=proxies)#, auth=auth)
                        headers = {'Content-Type' : 'application/json', 'Authorization' : bearer }
                        p = requests.options(conurl , headers=headers, proxies=proxies)#, auth=auth)
                        conurl = "https://api.spotify.com/v1/me/feature-flags?tests=tps_send_all_state_updates"
                        headers = {'Access-Control-Request' : 'authorization'}
                        p = requests.options(conurl , headers=headers, proxies=proxies)#, auth=auth)
                        headers = {'Access-Control-Request' : 'authorization'}
                        p = requests.options(conurl , headers=headers, proxies=proxies)#, auth=auth)
                        failed=5
                    except Exception as e:
                        failed=failed+1
                try:
                    device_dict = json.loads(message)
                    ######## simplify those array nesting, maybe saving them as variables one time externally and importing those
                    ####### these lines below appear multiple times so we have to clean those up
                    state_id = str(device_dict['payloads'][0]['state_machine']['states'][2]['state_id'])
                    t_id = int(device_dict['payloads'][0]['state_machine']['states'][2]['track'])
                    state_machine_id = str(device_dict['payloads'][0]['state_machine']['state_machine_id'])
                    n_duration = int(device_dict['payloads'][0]['state_machine']['tracks'][t_id]['metadata']['duration'])   
                    playback_id = str(device_dict['payloads'][0]['state_machine']['attributes']['playback_session_id'])
                    track_id = str(device_dict['payloads'][0]['state_machine']['tracks'][t_id]['metadata']['uri'])
                    artist_name = str(device_dict['payloads'][0]['state_machine']['tracks'][t_id]['metadata']['authors'][0]['name'])
                    track_name = str(device_dict['payloads'][0]['state_machine']['tracks'][t_id]['metadata']['name'])
                    manifest_id = str(device_dict['payloads'][0]['state_machine']['tracks'][t_id]['manifest']['file_ids_mp4'][0]['file_id'])
                    #print("cashify_play1")
                    ws.ws.send('{"type":"ping"}')
                    try:
                        import time
                        import math
                    except:
                        ok = 1
                    session_id = int(math.ceil(time.time() * 1000))
                    if(step==1):
                        ####### header line appears multiple times so that needs to be cleared up
                        headers = {'Content-Type' : 'application/json', 'Authorization' : bearer }
                        conurl = "https://api.spotify.com/v1/track-playback/v1/devices/"+device_id+"/state"
                        postData = ("""{"seq_num":SEQNUM,"state_ref":{"state_machine_id":"STATEMACHINEID","state_id":"STATEID","paused":false},"sub_state":{"playback_speed":1,"position":0,"duration":NDURATION,"stream_time":0},"debug_source":"before_track_load"}""").replace("SEQNUM",str(dev_seq)).replace("STATEMACHINEID",state_machine_id).replace("STATEID",state_id).replace("NDURATION",str(n_duration))
                        p = 1
                        p = requests.put(conurl, data=postData, headers=headers, proxies=proxies)#, auth=auth)
                        dev_seq = dev_seq + 1
                        pstring = str(p.content.decode('utf-8')).replace("b'{","{").replace("}'","}")
                        device_dict = json.loads(pstring)
                        state_machine_id = str(device_dict['state_machine']['state_machine_id'])
                        n_duration = int(device_dict['state_machine']['tracks'][t_id]['metadata']['duration'])   
                        playback_id = str(device_dict['state_machine']['attributes']['playback_session_id'])
                        artist_name = str(device_dict['state_machine']['tracks'][t_id]['metadata']['authors'][0]['name'])
                        track_name = str(device_dict['state_machine']['tracks'][t_id]['metadata']['name'])
                        ws.step = 2
                        ws.ws.send('{"type":"ping"}')
                        #print("cashify_play3")
                        headers = {'Content-Type' : 'application/json', 'Authorization' : bearer }
                        conurl = "https://api.spotify.com/v1/track-playback/v1/devices/"+device_id+"/state"
                        postData = ("""{"seq_num":SEQNUM,"state_ref":{"state_machine_id":"STATEMACHINEID","state_id":"STATEID","paused":false},"sub_state":{"playback_speed":1,"position":0,"duration":NDURATION,"stream_time":0},"previous_position":0,"debug_source":"position_changed"}""").replace("SEQNUM",str(dev_seq)).replace("STATEMACHINEID",state_machine_id).replace("STATEID",state_id).replace("NDURATION",str(n_duration))
                        p = requests.put(conurl, data=postData, headers=headers, proxies=proxies)#, auth=auth)
                        dev_seq = dev_seq + 1
                        string = str(p.content.decode('utf-8')).replace("b'{","{").replace("}'","}")
                        device_dict = json.loads(string)
                        state_machine_id = str(device_dict['state_machine']['state_machine_id'])
                        n_duration = int(device_dict['state_machine']['tracks'][t_id]['metadata']['duration'])   
                        playback_id = str(device_dict['state_machine']['attributes']['playback_session_id'])
                        artist_name = str(device_dict['state_machine']['tracks'][t_id]['metadata']['authors'][0]['name'])
                        track_name = str(device_dict['state_machine']['tracks'][t_id]['metadata']['name'])
                        ws.step = 3
                        #print("cashify_play4")
                        ws.ws.send('{"type":"ping"}')
                        postData = ("""{"seq_num":SEQNUM,"state_ref":{"state_machine_id":"STATEMACHINEID","state_id":"STATEID","paused":false},"sub_state":{"playback_speed":1,"position":0,"duration":NDURATION,"stream_time":500},"previous_position":0,"debug_source":"resume"}""").replace("SEQNUM",str(dev_seq)).replace("STATEMACHINEID",state_machine_id).replace("STATEID",state_id).replace("NDURATION",str(n_duration))
                        headers = {'Content-Type' : 'application/json', 'Authorization' : bearer }
                        conurl = "https://api.spotify.com/v1/track-playback/v1/devices/"+device_id+"/state"
                        p = requests.put(conurl, data=postData, headers=headers, proxies=proxies)#,auth=auth)
                        string = str(p.content.decode('utf-8')).replace("b'{","{").replace("}'","}")
                        device_dict = json.loads(string)
                        dev_seq = dev_seq + 1
                        state_machine_id = str(device_dict['state_machine']['state_machine_id'])
                        n_duration = int(device_dict['state_machine']['tracks'][t_id]['metadata']['duration'])   
                        playback_id = str(device_dict['state_machine']['attributes']['playback_session_id'])
                        conurl = "https://api.spotify.com/v1/storage-resolve/files/audio/interactive/"+str(manifest_id)+"?version=10000000&product=9&platform=39&alt=json"
                        headers = {'Access-Control-Request' : 'authorization'}
                        p = requests.options(conurl , headers=headers, proxies=proxies)#,auth=auth)
                        headers = {'Content-Type' : 'application/json', 'Authorization' : bearer }
                        g=1
                        g = requests.get(conurl, headers=headers, proxies=proxies)#,auth=auth)
                        string = str(g.content.decode('utf-8')).replace("b'{","{").replace("}'","}")
                        audio_dict = json.loads(string)
                        urljson = str(audio_dict['cdnurl'][0])
                        file_id = str(audio_dict['fileid'])
                        ws.step = 4
                        ws.ws.send('{"type":"ping"}')
                        headers = {'Content-Type' : 'application/json', 'Authorization' : bearer }
                        conurl = "https://api.spotify.com/v1/track-playback/v1/devices/"+device_id+"/state"
                        postData = ("""{"seq_num":SEQNUM,"state_ref":{"state_machine_id":"STATEMACHINEID","state_id":"STATEID","paused":false},"sub_state":{"playback_speed":1,"position":29939,"duration":NDURATION,"stream_time":60500},"previous_position":29939,"debug_source":"played_threshold_reached"}""").replace("SEQNUM",str(dev_seq)).replace("STATEMACHINEID",state_machine_id).replace("STATEID",state_id).replace("NDURATION",str(n_duration))
                        p = requests.put(conurl, data=postData, headers=headers, proxies=proxies)#,auth=auth)
                        dev_seq = dev_seq + 1
                        postData = ("""{"seq_num":SEQNUM,"state_ref":{"state_machine_id":"STATEMACHINEID","state_id":"STATEID","paused":false},"sub_state":{"playback_speed":1,"position":60001,"duration":NDURATION,"stream_time":121000},"previous_position":29939,"debug_source":"resume"}""").replace("SEQNUM",str(dev_seq)).replace("STATEMACHINEID",state_machine_id).replace("STATEID",state_id).replace("NDURATION",str(n_duration))
                        p = requests.put(conurl, data=postData, headers=headers, proxies=proxies)#,auth=auth)
                        dev_seq = dev_seq + 1
                        string = str(p.content.decode('utf-8')).replace("b'{","{").replace("}'","}")
                        device_dict = json.loads(string)
                        state_machine_id = str(device_dict['state_machine']['state_machine_id'])
                        n_duration = int(device_dict['state_machine']['tracks'][t_id]['metadata']['duration'])   
                        playback_id = str(device_dict['state_machine']['attributes']['playback_session_id'])
                        ws.step = 5
                        #print("cashify_play6")
                        ws.ws.send('{"type":"ping"}')
                        conurl = "https://api.spotify.com/v1/track-playback/v1/devices/"+device_id+"/state"
                        n_stime = int(n_duration*2.025)    
                        local_time = int(math.ceil(time.time() * 1000))
                        postData = ("""{"seq_num":SEQNUM,"state_ref":{"state_machine_id":"STATEMACHINEID","state_id":"STATEID","paused":false},"sub_state":{"playback_speed":1,"position":NDURATION,"duration":NDURATION,"stream_time":FINTIME},"previous_position":NDURATION,"playback_stats":{"ms_total_est":NDURATION,"ms_manifest_latency":155,"ms_latency":1285,"start_offset_ms":0,"ms_initial_buffering":1285,"ms_seek_rebuffering":0,"ms_stalled":0,"max_ms_seek_rebuffering":0,"max_ms_stalled":0,"n_stalls":0,"audiocodec":"mp4","time_weighted_bitrate":0,"key_system":"widevine","ms_key_latency":583,"total_bytes":8096469,"local_time_ms":LOCALTIME},"debug_source":"track_data_finalized"}""").replace("SEQNUM",str(dev_seq)).replace("STATEMACHINEID",state_machine_id).replace("STATEID",state_id).replace("FINTIME",str(n_stime)).replace("NDURATION",str(n_duration)).replace("LOCALTIME",str(local_time+n_duration+2023))
                        p = requests.put(conurl, data=postData, headers=headers, proxies=proxies)#,auth=auth)
                        thisis = str("proc:"+str(ws.mynr)+" => "+str(device_name)+" | ARTIST: "+str(artist_name)+" | TRACK: "+str(track_name)+" | DONE: "+str("%.2f" % float(n_duration/1000/60))+"/"+str("%.2f" % float(n_duration/1000/60))+" MIN | "+ws.proxy)
                        cprint(thisis,'cyan')
                        ws.que.put(thisis)
                        dev_seq = dev_seq + 1
                        realsent.value +=1
                        ws.ws.send('{"type":"ping"}')
                        #print("cashify_play7")
                        string = str(p.content.decode('utf-8')).replace("b'{","{").replace("}'","}")
                        device_dict = json.loads(string)
                        state_machine_id = str(device_dict['state_machine']['state_machine_id'])
                        n_duration = int(device_dict['state_machine']['tracks'][t_id]['metadata']['duration'])   
                        playback_id = str(device_dict['state_machine']['attributes']['playback_session_id'])
                        next_playback_id = str('%032x' % random.getrandbits(128))
                        playback_id = state_id
                        conurl = "https://api.spotify.com/v1/melody/v1/logging/track_stream_verification"
                        headers = {'Access-Control-Request' : 'authorization'}
                        p = requests.options(conurl , headers=headers, proxies=proxies)#,auth=auth)
                        conurl = "https://api.spotify.com/v1/melody/v1/logging/jssdk_playback_stats"
                        headers = {'Access-Control-Request' : 'authorization'}
                        d=1
                        #print("cashify_play8")
                        ws.ws.send('{"type":"ping"}')
                        d = requests.options(conurl , headers=headers, proxies=proxies)#,auth=auth)
                        headers = {'Content-Type' : 'application/json', 'Authorization' : bearer }
                        conurl = "https://api.spotify.com/v1/melody/v1/logging/track_stream_verification"
                        postData = ("""{"sdk_id":"harmony:3.19.1-441cc8f","platform":"Partner public_js-sdk harmony-DEVPLAT.76-DEVOS","play_track":"TRACKID","playback_id":"PLAYBACKID","ms_played":NDURATION,"session_id":"SESSIONID","sequence_id":SEQID,"next_playback_id":"NEXTPLAYID"}""").replace("SEQNUM",str(dev_seq)).replace("STATEMACHINEID",state_machine_id).replace("STATEID",state_id).replace("FINTIME",str(n_stime)).replace("NDURATION",str(n_duration)).replace("DEVOS",dev_os).replace("DEVPLAT",str(dev_platf)).replace("PLAYBACKID",str(playback_id)).replace("SEQID",str(seq_id)).replace("NEXTPLAYID",str(next_playback_id)).replace("SESSIONID",str(session_id)).replace("TRACKID",str(track_id))
                        p = requests.post(conurl, data=postData, headers=headers, proxies=proxies)#,auth=auth)
                        string = p.content
                        didsave = False
                        #print("cashify_play9")
                        proxies = { "https" : "http://"+str(ws.proxy) }
                        failed = 0
                        while(failed<3):
                            try:
                                if(failed == 1):
                                    nprx = str(ws.proxy).split(':')[0]+':'+str(int(str(ws.proxy).split(':')[1])+1)
                                    proxies = { "https" : "http://"+str(nprx) }
                                if(failed == 2):
                                    nprx = str(ws.proxy).split(':')[0]+':'+str(int(str(ws.proxy).split(':')[1])+1)
                                    proxies = { "https" : "http://"+str(nprx) }
                                
                                reason = random.choice(['remote','trackdone','trackdone']) ##### what is the purpos of having duplicat choices
                                if(random.randint(0,100) < int(8)):
                                    didsave = True
                                    headers = {'Content-Type' : 'application/json', 'Authorization' : bearer }
                                    postData = ("""{"sdk_id":"harmony:3.19.1-441cc8f","platform":"Partner public_js-sdk harmony-DEVPLAT.76-DEVOS","play_track":"TRACKID","file_id":"FILEID","playback_id":"PLAYBACKID","internal_play_id":"SEQID","memory_cached":true,"persistent_cached":true,"audio_formsat":"mp4","video_format":null,"manifest_id":"MANIFESTID","protected":true,"key_system":"com.widevine.alpha","key_system_impl":"native","urls_json":"{\\"version\\":\\"1.0.0\\",\\"urls\\":\\"[{\\"url\\":\\"URLJSON\\",\\"segments\\":25,\\"avg_bw\\":29172999.1142516}]\\"}","start_time":STARTTIME,"end_time":ENDTIME,"external_start_time":0,"ms_play_latency":963,"ms_init_latency":553,"ms_head_latency":775,"ms_manifest_latency":130,"ms_resolve_latency":85,"ms_license_generation_latency":158,"ms_license_request_latency":93,"ms_license_session_latency":128,"ms_license_update_latency":201,"ms_played":"""+str(n_duration)+""","ms_nominal_played":"""+str(n_duration)+""","ms_file_duration":"""+str(n_duration)+""","ms_actual_duration":"""+str(n_duration)+""","ms_start_position":0,"ms_end_position":"""+str(n_duration)+""","ms_seek_rebuffer":0,"ms_seek_rebuffer_longest":0,"ms_stall_rebuffer":0,"ms_stall_rebuffer_longest":0,"n_stalls":0,"n_seekback":0,"n_seekforward":0,"start_bitrate":null,"time_weighted_bitrate":0,"reason_start":\""""+str(reason)+"""","reason_end":"trackdone","initially_paused":false,"had_error":false,"n_warnings":0,"n_navigator_offline":0}""").replace("DEVOS",str(dev_os)).replace("DEVPLAT",str(dev_platf)).replace("PLAYBACKID",str(playback_id)).replace("MANIFESTID",str(manifest_id)).replace("TRACKID",track_id).replace("FILEID",file_id).replace("SEQID",str(seq_id)).replace("STARTTIME",str(local_time)).replace("ENDTIME",str(local_time+n_duration+2023))
                                    #print("cashify_play9")
                                else:
                                    headers = {'Content-Type' : 'application/json', 'Authorization' : bearer }
                                    postData = ("""{"sdk_id":"harmony:3.19.1-441cc8f","platform":"Partner public_js-sdk harmony-DEVPLAT.76-DEVOS","play_track":"TRACKID","file_id":"FILEID","playback_id":"PLAYBACKID","internal_play_id":"SEQID","memory_cached":false,"persistent_cached":false,"audio_formsat":"mp4","video_format":null,"manifest_id":"MANIFESTID","protected":true,"key_system":"com.widevine.alpha","key_system_impl":"native","urls_json":"{\\"version\\":\\"1.0.0\\",\\"urls\\":\\"[{\\"url\\":\\"URLJSON\\",\\"segments\\":25,\\"avg_bw\\":29172999.1142516}]\\"}","start_time":STARTTIME,"end_time":ENDTIME,"external_start_time":0,"ms_play_latency":963,"ms_init_latency":553,"ms_head_latency":775,"ms_manifest_latency":130,"ms_resolve_latency":85,"ms_license_generation_latency":158,"ms_license_request_latency":93,"ms_license_session_latency":128,"ms_license_update_latency":201,"ms_played":"""+str(n_duration)+""","ms_nominal_played":"""+str(n_duration)+""","ms_file_duration":"""+str(n_duration)+""","ms_actual_duration":"""+str(n_duration)+""","ms_start_position":0,"ms_end_position":"""+str(n_duration)+""","ms_seek_rebuffer":0,"ms_seek_rebuffer_longest":0,"ms_stall_rebuffer":0,"ms_stall_rebuffer_longest":0,"n_stalls":0,"n_seekback":0,"n_seekforward":0,"start_bitrate":null,"time_weighted_bitrate":0,"reason_start":\""""+str(reason)+"""","reason_end":"trackdone","initially_paused":false,"had_error":false,"n_warnings":0,"n_navigator_offline":0}""").replace("DEVOS",str(dev_os)).replace("DEVPLAT",str(dev_platf)).replace("PLAYBACKID",str(playback_id)).replace("MANIFESTID",str(manifest_id)).replace("TRACKID",track_id).replace("FILEID",file_id).replace("SEQID",str(seq_id)).replace("STARTTIME",str(local_time)).replace("ENDTIME",str(local_time+n_duration+2023))
                                    #print("cashify_play9")
                                conurl = "https://api.spotify.com/v1/melody/v1/logging/jssdk_playback_stats" 
                                ###
                                p = requests.post(conurl, data=postData, headers=headers, proxies=proxies)#,auth=auth)
                                if(p.status_code == 202):                    
                                    string = p.content
                                    writeCount(ws, str(ti))
                                    failed=5
                                else:
                                    ok=1
                                failed =5
                            except:
                                failed+=1
                        ws.ws.send('{"type":"ping"}')
                        if(random.randint(0,100) >= int(nautof) and autof == "True"):
                            sp = ws.sp
                            pb = sp.current_playback(market=None)
                            try:
                                owid = str(sp.me()['id'])                 
                                pllid = str(pb['context']['uri']).split(':')[2]
                                sp.user_playlist_follow_playlist(owid, pllid)
                                follows.value+=1
                            except:
                                fuck = 'this'
                        if(didsave and autos == "True"):
                            pb = sp.current_playback(market=None)
                            try:
                                iid = str(pb['item']['id'])
                                reswww = re.search('spotify:artist:(.*)\'', str(pb))
                                resw = str(reswww.group(1)).split("'")[0] 
                                check = sp.current_user_saved_tracks_contains(tracks=['spotify:track:'+str(iid)])
                                if('alse' in str(check)):
                                    sp.current_user_saved_tracks_add(tracks=[iid])  #### checks if user saves track
                                    savess.value +=1
                                    try:
                                        if(random.randint(0,10) > 5):
                                            sp.user_follow_artists(ids=[resw])
                                            follows.value+=1
                                    except:
                                        wtf = 1
                            except:
                                wtf = 1
                        if(ws.cp == True):
                            sp.user_playlist_unfollow(ws.mid, ws.lid)
                        tenum = threading.enumerate()
                        for ot in tenum:
                            if('ws'+str(ws.mynr) in ot.name):
                                terminate_thread(ot)
                                break
                            elif(ws.name in ot.name):
                                if(str(ws.mynr) in ot.name):
                                    if(not 'checker' in ot.name):
                                        terminate_thread(ot)
                                        break

                except Exception as exi:
                    #cprint(exi,'yellow')             
                    ok =1             
            if(":{\"Spotify-Connection-Id\":" in message):  
                result = re.search('Spotify-Connection-Id":"(.*)="},"method"', str(message))
                keyy = str(result.group(1))
                try:
                    ws.token, ws.sp, ws.dev_seq = createDevice(ws, ws.ws.token, keyy, ws.nautof, ws.nautos)
                    ws.ppl = ws.plid
                except Exception as e:
                    ok=1
                failed = True
                try:
                    if(('track' in ws.ppl)):
                        try:
                            if random.randint(0,100) <= int(33):
                                #ADD TRACK TO NEW PLAYLIST
                                me = ws.sp.me()
                                mname = me['display_name']
                                mid = me['id']
                                lname = 'FrkyFrDay777'
                                #cprint(mname+' @id: '+str(mid)+' creating FrkyFrDay777..','yellow')
                                lists = ws.sp.user_playlists(mid, limit=5, offset=0)
                                lid = 0
                                for listitem in lists['items']:
                                    if(listitem['name'] == lname):
                                        lid = listitem['id']
                                if( lid == 0 ):
                                    ws.sp.user_playlist_create(mid, lname, public=False, description='')
                                    #wait for list to get recognized
                                    time.sleep(2)
                                    lists = ws.sp.user_playlists(mid, limit=5, offset=0)
                                    for listitem in lists['items']:
                                        if(listitem['name'] == lname):
                                            lid = listitem['id']
                                    #add tracks
                                    ws.mid = mid
                                    ws.lid = lid
                                    ws.cp = True
                                    if(lid != 0):
                                        ws.sp.user_playlist_add_tracks(str(mid), str(lid), [ws.ppl], position=None)
                                        time.sleep(1)
                                        #cprint('added and streaming track via playlist..','yellow')
                                        ws.sp.start_playback(device_id=ws.device_id,context_uri=ws.ppl,offset={"position": str(0)})
                                    else:
                                        lists = ws.sp.user_playlists(mid, limit=3, offset=0)
                                        for listitem in lists['items']:
                                            if(listitem['name'] == lname):
                                                lid = listitem['id']
                                        ws.sp.user_playlist_add_tracks(str(mid), str(lid), [ws.ppl], position=None)
                                        ws.ppl = 'spotify:playlist:'+str(lid)
                                        #cprint('added and streaming track via playlist..','yellow')
                                        ws.sp.start_playback(device_id=ws.device_id,context_uri=ws.ppl,offset={"position": str(0)})
                                else:
                                    ws.sp.user_playlist_unfollow(mid, lid)
                                    time.sleep(1)
                                    ws.sp.user_playlist_create(mid, lname, public=False, description='')
                                    #wait for list to get recognized
                                    time.sleep(2)
                                    lists = ws.sp.user_playlists(mid, limit=3, offset=0)
                                    for listitem in lists['items']:
                                        if(listitem['name'] == lname):
                                            lid = listitem['id']
                                    #add tracks
                                    ws.mid = mid
                                    ws.lid = lid
                                    ws.cp = True
                                    if(lid != 0):
                                        ws.sp.user_playlist_add_tracks(str(mid), str(lid), [ws.ppl], position=None)
                                        time.sleep(1)
                                        ws.ppl = 'spotify:playlist:'+str(lid)
                                        ws.sp.start_playback(device_id=ws.device_id,context_uri=ws.ppl,offset={"position": str(0)})
                                    else:
                                        lists = ws.sp.user_playlists(mid, limit=3, offset=0)
                                        for listitem in lists['items']:
                                            if(listitem['name'] == lname):
                                                lid = listitem['id']
                                        ws.sp.user_playlist_add_tracks(str(mid), str(lid), [ws.ppl], position=None)
                                        time.sleep(1)
                                        ws.sp.start_playback(device_id=ws.device_id,context_uri=ws.ppl,offset={"position": str(0)})
                            else:
                                ws.sp.start_playback(device_id=ws.device_id,uris=[ws.ppl])
                        except:
                            ws.sp.start_playback(device_id=ws.device_id,uris=[ws.ppl])
                    elif('artist' in ws.ppl):
                        ws.sp.start_playback(device_id=ws.device_id,context_uri=ws.ppl)                        
                    else:
                        #print("playlist: "+str(ws.ppl)+" position: "+str(int(ws.tpos)-1))
                        ws.sp.start_playback(device_id=ws.device_id,context_uri=ws.ppl,offset={ "position": str(int(ws.tpos)-1)})
                    failed = False
                except Exception as e:
                    if('track' in ws.ppl):
                        ws.sp.start_playback(device_id=ws.device_id,uris=[ws.ppl])
                    else:
                        ws.sp.start_playback(device_id=ws.device_id,context_uri=ws.ppl,offset={ "position": str(int(ws.tpos)-1) })
            if(('application/json"},"payloads":[{"type":"replace' in str(message)) and ('playback_session_id":""' not in str(message))):
                try:
                    cashify_play(ws, message, ws.token, ws.ws.dev_seq, ws.step, ws.dev_os, ws.dev_platf, ws.seq_id, ws.autof, ws.nautof, ws.autos, ws.nautos, ws.device_id, ws.plid, ws.var50k, ws.proxy, ws.sp, ws.device_name, ws.useprox,ws.oout,ws.savess,ws.follows,ws.realsent)
                except Exception as e:
                    cprint(str(e),'red')
                    ok =1
        def on_error(ws, error):
            ok = 1
        def on_close(ws):
            ok=1
        def on_open(ws): ##### gotta remove all the unnecessary error checks
            def run(ws): 
                for _ in range(10):
                    try:
                        ws.send('{"type":"ping"}')
                    except Exception as e:
                        ok=1
                    res = time.sleep(5)
                ws.killme()
                ws.terminate_thread(ws.wst)
            run()    
        def killme(self):
            self.ws.keep_running = False
        def run(self):
            try:
                websocket.enableTrace(False)
                self.ws = websocket.WebSocketApp("wss://gew-dealer.spotify.com/?access_token="+str(self.token),
                                          on_message = self.on_message,
                                          on_error = self.on_error,
                                          on_close = self.on_close
                                          )
                self.ws.on_open = self.on_open
                self.ws.dev_seq = 0
                self.ws.keep_running = True
                self.ws.tplay = 0
                self.ws.msg = "first"
                self.ws.token = self.token
                self.ws.proxy = "https://"+self.proxy
                self.wst = 1
                self.ws.que = self.que
                
                if "@" in str(self.proxy):
                    self.wst = Thread(target=self.ws.run_forever, kwargs={'http_proxy_host':str(self.proxy.split(':')[0])+str(self.proxy.split(':')[1]),'http_proxy_port':int(self.proxy.split(':')[-1]),'sslopt': ssl.CERT_NONE}, name=str(self.name)+'ws'+str(self.mynr))
                else:
                    #self.wst = Thread(target=self.ws.run_forever, kwargs={'http_proxy_host':str(self.proxy.split(':')[0]),'http_proxy_port':int(self.proxy.split(':')[1]),'http_proxy_auth':(self.proxyuser, self.proxypass),'sslopt': ssl.CERT_NONE}, name=str(self.name)+'ws'+str(self.mynr))
                    self.wst = Thread(target=self.ws.run_forever, kwargs={'http_proxy_host':str(self.proxy.split(':')[0]),'http_proxy_port':int(self.proxy.split(':')[1]),'sslopt': ssl.CERT_NONE}, name=str(self.name)+'ws'+str(self.mynr))
                self.wst.deamon = False
                started = False
                self.wst.start()
                started = True
            except Exception as e:
                cprint(e,'red')
                ok=1
            return

    proz=1
    waited = 0
    excepted = 0
    didit = False
    lt = len(t_chunk)
    
    def getwork(): ###### function is to ask what orders do i have from boombox (database of artists who ordered for streams)
        failed=True
        work = []
        while(failed):
            try:
                connection_obj = connection_pool.get_connection()
                cur = connection_obj.cursor()
                cur.execute('SELECT * FROM boombox.orders WHERE orders.max24>=orders.did24 AND done=0')
                work = cur.fetchall()
                connection_obj.close()
                thistarget = random.choice(work)
                failed=False
            except Exception as e:
                time.sleep(1)
        return thistarget
    def finishwork(id):
        failed=True
        work = []
        while(failed):
            try:
                connection_obj = connection_pool.get_connection()
                cur = connection_obj.cursor()
                cur.execute("UPDATE orders SET done=1 WHERE id="+id+"")
                connection_obj.close()
                failed=False
            except Exception as e:
                time.sleep(random.randint(1,2))
        return "ok"
    def getprox(ccode):  #### most important
        ###### we need to check always where our user lives
        ###### so if you say that we need to have the proxy BEFORE we even start running the script, does that mean this function needs to be rewritten in another script if we don't need it here?
        global rtime
        try:
            connection_obj = connection_pool.get_connection()
            cur = connection_obj.cursor()
            cur.execute('SELECT proxy FROM proxies WHERE country="'+ccode+'"')
            myresult = cur.fetchone()
            if myresult != None:
                connection_obj.close()
                if("xiware" in str(myresult[0])):
                    px = str(myresult[0])
                    rtime=45
                    return str(px)
                if("xyrack" in str(myresult[0])):
                    px = str(myresult[0])
                    rtime=65
                    return str(px)
                if("smartproxy" in str(myresult[0])):
                    px = str(myresult[0])
                    rtime=65
                    return str(random.choice(["city.smartproxy.com:21000","city.smartproxy.com:21100","city.smartproxy.com:21150","city.smartproxy.com:21200"]))
            ##### never run this locally, cause locations give away where these computers are coming from
            else:
                #NO PROXY FOR THIS COUNTRY taking INT
                cur.execute('SELECT proxy FROM proxies WHERE country="INT"')
                myresult = cur.fetchone()
                connection_obj.close()
                if("xiware" in str(myresult[0])):
                    px = str(myresult[0])
                    rtime=45
                    return str(px)
                if("xyrack" in str(myresult[0])):
                    px = str(myresult[0])
                    rtime=65
                    return str(px)
                if("smartproxy" in str(myresult[0])):
                    px = str(myresult[0])
                    rtime=65
                    return str(px)                
        except:
            print('no db connection..')
    while(didit is False):
        if excepted == 5:
            killAll()
            excepted = 0
            gc.collect()
        try:
            _FINISH = False
            mmm = 0
            excis = 0
            faulted = False
            gc.collect()
            openup = True
            #statuschange("working")
            while(openup):
                for v in range(lt):
                    try:
                        acc = t_chunk.pop(0)
                        acc=acc.replace(" bB", "B").strip()
                        thistarget = getwork()
                        thisId=str(thistarget[0])
                        thisTargetLink=str(thistarget[2])
                        thisPos=thistarget[3]
                        thisAmount=thistarget[4]
                        thisMax24=thistarget[5]
                        thisDid24=thistarget[6]
                        thisDidTotal=thistarget[7]
                        thisCcode=thistarget[8]
                        thisDone=thistarget[9]
                        #checkifdone
                        if(thisAmount<=thisDidTotal):
                            finishwork(thisId)
                            break
                        else:
                            prox = str(random.choice(["city.smartproxy.com:21000","city.smartproxy.com:21100","city.smartproxy.com:21150","city.smartproxy.com:21200","city.smartproxy.com:21000","city.smartproxy.com:21100","city.smartproxy.com:21150","city.smartproxy.com:21200","city.smartproxy.com:21250"]))#getprox(thisCcode)
                            auth = "a:b"##str(random.choice(authstr[:-1])).rstrip()+":"+str(authstr[-1]).rstrip()
                            taaa = hackify(str(acc).rstrip(),prox,auth,mmm,"round"+str(round.value), q ,connection_pool, autos, nautos, autof, nautof, ipmode, ipconf, thisTargetLink, thisPos, 100000000, "y", follows, savess, realsent, thisId, percentage)
                            taaa.run()
                            time.sleep(0.2)
                            mmm=mmm+1
                            excis = 0
                    except Exception as e:
                        #cprint(e,'red')
                        errshit = 1
                openup = False
            time.sleep(62)
            mmm = 0
            didit = True
            os._exit(0)
        except Exception as e:
            cprint(e,'yellow')
            excepted +=1
            os.exit(0)

if __name__ == "__main__":
    global nr, plid, tpos, pnr1, pnr2, plen1, plen2, oout, stop, kstop, autos, nautos, autof, nautof, ipmode, ipconf, modus, sleepafter, sleepfor, s, rtime
    multiprocessing.freeze_support()
    s = socket.socket()
    given_id = Value('i',0)
    ik = 1
    bot=1
    db = 1
    cur = 1
    pf=1
    spm = 0
    aspm = 0
    sser = 17
    authed = 0
    elapsed = 0
    savess = Value('i',0)
    follows = Value('i',0)
    realsent = Value('i', 0)
    round = Value('i', 0)
    nr = 250
    plid= []
    tpos= []
    pnr1 = 30
    pnr2 = 50000000000000
    plen1= ""
    plen2= 250
    oout = ""
    stop = 10000000000
    kstop = 10000000000
    autos = True
    nautos = 7
    autof = 0
    nautof = 0
    ipmode = "rotprox"
    ipconf = ""
    modus = ""
    sleepafter = 9999999999999999999999
    sleepfor = 600
    useprox = 'y'
    new = 'n'
    tric = 'a'
    file = ''
    status = 'on'
    config= {'host':'191.101.192.57', 'user':'user', 'password':'password', 'database':'boombox', 'autocommit':True}
    connection_pool = 1
    accounts = []
    avabac = []
    accas = []
    t_data = []
    threadis = []
    proxy_list = []
    my_data = []

    def randSleep(secs):
        time.sleep(1 * 1 * secs)
        result = 39 * 2
        return result
    
    def waitNsec(secs):
        result = randSleep(secs)
        return result
    
    def renewAcc():
        global accounts
        #file = open(str(sys.argv[1]), 'r')
        #accounts = file.readlines()
        ok=1

    def fuckyou(authed):
        if(authed is not savess):
            if(authed is not ik):
                resi=tric+ik
    
    def chunkIt(seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0
        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg
        return out
    
    def renewList():
        global avabac, accounts, plen2
        avabac = chunkIt(accounts, int(plen2))
        return True
        
    def popAcc(mmm):
        global avabac,accas
        try:
            acci = accas[mmm].pop()
        except:
            accas[mmm] = avabac[mmm].copy()
            acci = accas[mmm].pop()
        return acci.rstrip()
    
    def terminate_thread(thread):
        if not thread.isAlive():
            return
        exc = ctypes.py_object(SystemExit)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
            ctypes.c_long(thread.ident), exc)
        if res == 0:
            raise ValueError("nonexistent thread id")
        elif res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
    
    def checkagain():
        global authed
        if authed == int(savess)+2:
            fuckyou(authed)
    
    def cacvate():
        global lkey,authed
        lkey = lkey[0]
        pubKey = "<RSAKeyValue><Modulus>rlXUqfGZRfh556DgurmqytOUOLem3yjl/3YWjEpGBSLk/qa8SQ8jAL7fHpa8k8IxHwtdBeiLtQBGRH1M5Bbjc+3IxASiUElZiB1L5xuuG4cjUdCxph2h4pMu/8rny0mkHFAsEOCY+vwqsm3ap5iDMUtYqVw0b4+5nRe3DwAaS1qsPOQjAm9Hk0pGZ6sSV7CWfyxS6IwMiaEg8JSA9S1r3y7r5DRo3uGfEmtrRzXLECZji1ySYmbXu+CZDoXvN/FMfLQapc8qwV7kPz4z11LEZJAc+zwjMhnVKB8oGWfn/YD1dY0axl84IiTDlSCjhhgQ/dNvZNrNXR0XIFNZcmWsOw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
        res = Key.activate(token="WyIxMDUxNiIsInU3NmZFYStmYUN2SHpQanFPSzBpdHpHeXY5bnY4emFuL3RiRUhOUUciXQ==", rsa_pub_key=pubKey, product_id=5196, key=lkey.rstrip(), machine_code=Helpers.GetMachineCode())
        if res[0] == None or not Helpers.IsOnRightMachine(res[0]):
            fuckyou(authed)
        else:
            authed=ik
    
    def getCount(tplay,name):
        global connection_pool
        sql = "SELECT counter."+str(tplay)+" FROM counter WHERE counter.name="+str(name)
        failed=True
        count = 1
        while(failed):
            try:
                connection_obj = connection_pool.get_connection()
                cur = connection_obj.cursor()
                cur.execute(sql)
                myresult = cur.fetchone()
                count = int(myresult[0])
                connection_obj.close()
                failed=False
            except Exception as e:
                time.sleep(random.randint(1,3))
        return count                          
    
    def spmCalc(realsent):
        global spm, aspm, elapsed
        snrr = 0
        while(True):
            time.sleep(10)
            try:
                aspm = int(realsent.value)/int(elapsed)
            except: aspm=0
            snrr = snrr+1
            if(snrr==6):
                elapsed = elapsed+1
                snrr = 0
    
    def prinFuckr():
        global t_data
        os.system('cls')
        cprint('\n#--== ONE DAY THIS WORK WILL PAY ==--#\n','magenta')
        cprint("\nrunning cash play","green")
        cprint("snatched " + str(len(t_data)) + " spotify tokens..\n","green")
    
    def writer(savess,follows,realsent,round, q, oout):
        global nr, authed, spm, aspm, t_data
        myqueue = []
        cpcc = multiprocessing.cpu_count()
        written = 0
        while(True):
            try:
                myqueue.append(q.get())
                if(len(myqueue)>10):
                    for msg in myqueue:
                        try:
                            if written == 15:
                                os.system('cls')
                                prinFuckr()
                                print('\n')
                                written = 0
                            ctypes.windll.kernel32.SetConsoleTitleW("s0pBeast v3.2 mCore -- [THREADS]: "+str(100)+" -- [ROUND]: "+str(round.value)+" -- [STREAMS]: "+str(realsent.value)+" -- [ELAPSED]: "+str(elapsed))
                            _msg_nr = int(msg.split(" ")[-1].rstrip())
                            plh = " "+str(_msg_nr)
                            #cprint(str(msg),'cyan')
                            fuckyou(authed)
                            while not q.empty():
                                myqueue.append(q.get())
                            mysleep = int(100/len(myqueue))
                            written+=1
                            if mysleep < 0.2:
                               time.sleep(0.2)
                            else:
                               time.sleep(mysleep)
                        except:
                               time.sleep(0.5)
                    myqueue = []
                else:
                    time.sleep(0.03)
            except Exception as e:
                time.sleep(1)
                myqueue.append(q.get())
                
    def writeCoun(lkey,pkey,tkk):
        global authed
        lkey = lkey[0]
        pubKey = pkey
        res = Key.activate(token=tkk, rsa_pub_key=pubKey, product_id=5196, key=lkey.rstrip(), machine_code=Helpers.GetMachineCode())
        if res[0] == None or not Helpers.IsOnRightMachine(res[0]):
            fuckyou(authed)
        else:
            authed=ik
    
    def greet(accounts):
        cprint("\nstarting cash play","green")
        cprint("loaded " + str(len(accounts)) + " spotify accounts..\n","green")
    
    def prinFuck():
        global accounts, new, useprox
        cprint('\n#--== ONE DAY THIS WORK WILL PAY ==--#\n','magenta')

    def killer(thrnd):
        gogo = True
        time.sleep(26)
        tenum = threading.enumerate()
        print(tenum)
        for ot in tenum:
            if('round'+str(thrnd) in ot.name):
                if('ws' in ot.name):
                    terminate_thread(ot)
                    time.sleep(0.2)
                    print('shot one!')
        return True 
    
    def waitTheFuck():
        global t_data, my_data
        goOn = True
        while(goOn):
            ldat = len(t_data)
            cprint('\nsnatched '+str(len(t_data))+' tokens','cyan')
            time.sleep(6)
            if(len(t_data) == ldat):
                goOn = False
            if(len(t_data) <= 1000):
                my_data = t_data.copy()
                goOn = True
            os.system('cls')
            prinFuck()
            cprint('\nbeast is warming up, can take a while..','yellow')
        return 'yaah'
    
    def waitTheFuckagain():
        global t_data, my_data
        goOn = True
        while(goOn):
            ldat = len(t_data)
            cprint('\nsnatched '+str(len(t_data))+' tokens','cyan')
            time.sleep(6)
            if(len(t_data) == ldat):
                goOn = False
            if(len(t_data) <= 1000):
                my_data = t_data.copy()
                goOn = True
            #os.system('cls')
            #prinFuck()
            #cprint('\nbeast is warming up, can take a while..','yellow')
        return 'yaah'
    
    def getacc1():  
        sc = socket.socket()
        host = "191.101.192.57"
        port = 28711
        failed = True
        while(failed):
            try:
                sc.connect((host, port))
                sc.send('s0p'.encode())
                tkn_resp = sc.recv(84384)
                sc.close()
                tkn_list = str(tkn_resp).replace('b"[','').replace(']"','').replace("'","").split(',')
                return tkn_list
                failed = False
            except Exception as e:
                sc = socket.socket()
                time.sleep(5)
    
    def getacc(db_tbl,first_id):
        global given_id
        pub_tokens = []
        last3k = []
        connect_db_host = '38.68.41.18'
        try:
            connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="py_pool_mn", pool_size=int(20), pool_reset_session=True, host=connect_db_host, database='tokenbox', user='admin', password='boombox', autocommit=True)
        except:
            print("mysqlerror, can not connect to db on "+connect_db_host)
            os._exit(0)
 
        while True:
            try:
                #fetch 5k
                failed=True
                fresh_tokens = []
                while(failed):
                    try:
                        connection_obj = connection_pool.get_connection()
                        cur = connection_obj.cursor()
                        cur.execute('SELECT atkn FROM tokenbox.'+db_tbl+' WHERE id>='+str(given_id)+' and id<'+str(given_id+100)+' ORDER BY id ASC')
                        given_id+=100
                        fresh_tokens = cur.fetchall()
                        connection_obj.close()
                        failed=False
                    except Exception as e:
                        time.sleep(1)
                temp_tkn = []
                for tkn in fresh_tokens:
                    tkn = str(tkn).replace('(','').replace(',','').replace(')','').replace(" ","").replace("'","")
                    temp_tkn.append(tkn)
                fresh_tokens = []
                pub_tokens = temp_tkn.copy()
                temp_tkn = []
                if(len(last3k)<100):
                    given_id = int(str(first_id[0]).replace("(","").replace(")","").replace(",","").replace(" ","")) 
                    failed=True
                    fresh_tokens = []
                    while(failed):
                        try:
                            connection_obj = connection_pool.get_connection()
                            cur = connection_obj.cursor()
                            cur.execute('SELECT atkn FROM tokenbox.'+db_tbl+' WHERE id>='+str(given_id)+' and id<'+str(given_id+(100-len(last3k)))+' ORDER BY id ASC')
                            given_id+=(100-len(last3k))
                            fresh_tokens = cur.fetchall()
                            connection_obj.close()
                            failed=False
                        except Exception as e:
                            time.sleep(1)
                    temp_tkn = []
                    for tkn in fresh_tokens:
                        tkn = str(tkn).replace('(','').replace(',','').replace(')','').replace(" ","").replace("'","")
                        temp_tkn.append(tkn)
                    fresh_tokens = []
                    pub_tokens.append(temp_tkn)
                    temp_tkn = []                
                #return them
                return pub_tokens
            except Exception as e:
                print(e)
    
    ctypes.windll.kernel32.SetConsoleTitleW("spBeast v4.1 sp -- BigBoyToolz -- 2020")
    useprox = 'y'
    percentage = int(33)

    connect_db_host = '191.101.192.57'
    try:
        connect_db_file = open("host.txt","r")
        connect_db_host = connect_db_file.readline().rstrip()
        connect_db_file.close()
    except:
        cprint("can not find host.txt, trying to connect to good ol' mama africa..","yellow")
        connect_db_host = '191.101.192.57'
    try:
        connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="py_pool_main", pool_size=int(20), pool_reset_session=True, host=connect_db_host, database='boombox', user='admin', password='boombox', autocommit=True)
    except:
        cprint("mysqlerror, can not connect to db on "+connect_db_host,"red")
        os._exit(0)
    
    conni_db_host = '191.101.192.57'
    try:
        conni_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="py_pool_ma", pool_size=int(2), pool_reset_session=True, host=conni_db_host, database='boombox', user='user', password='password', autocommit=True)
    except:
        print("mysqlerror, can not connect to db on "+conni_db_host)
        os._exit(0)
    
    conni_obj = conni_pool.get_connection()
    curi = conni_obj.cursor(buffered=True)
    curi.execute('set global max_connections = 15000;')
    
    curi.execute('SELECT id FROM cookies ORDER BY id ASC')
    first_id = curi.fetchall()
    conni_obj.close()
    #print(first_id[0])
    given_id = Value('i',int(str(first_id[0]).replace("(","").replace(")","").replace(",","").replace(" ","")))       
    connection_obj = connection_pool.get_connection()
    cur = connection_obj.cursor(buffered=True)
    cur.execute('set global max_connections = 15000;')
    manager = multiprocessing.Manager()
    q = manager.Queue()
    os.system('cls')
    prinFuck()
    pkey = "<RSAKeyValue><Modulus>rlXUqfGZRfh556DgurmqytOUOLem3yjl/3YWjEpGBSLk/qa8SQ8jAL7fHpa8k8IxHwtdBeiLtQBGRH1M5Bbjc+3IxASiUElZiB1L5xuuG4cjUdCxph2h4pMu/8rny0mkHFAsEOCY+vwqsm3ap5iDMUtYqVw0b4+5nRe3DwAaS1qsPOQjAm9Hk0pGZ6sSV7CWfyxS6IwMiaEg8JSA9S1r3y7r5DRo3uGfEmtrRzXLECZji1ySYmbXu+CZDoXvN/FMfLQapc8qwV7kPz4z11LEZJAc+zwjMhnVKB8oGWfn/YD1dY0axl84IiTDlSCjhhgQ/dNvZNrNXR0XIFNZcmWsOw==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
    file = open("nlicense.ini","r")
    lkey = file.readlines()
    file.close()
    round = Value('i',1)
    savess = Value('i',0)
    follows = Value('i',0)
    realsent = Value('i', 0)
    rtime = Value('i', 65)
    __Finish = False
    _FINISH = False
    wout = Thread(target=writer, name="writer", args= (savess,follows,realsent,round,q,oout))
    wout.start()
    spmt = Thread(target=spmCalc, name="spm", args=[realsent])
    spmrunning = False
    tkk = "WyIxMDUxNiIsInU3NmZFYStmYUN2SHpQanFPSzBpdHpHeXY5bnY4emFuL3RiRUhOUUciXQ=="
    cacvate()
    oner = writeCoun(lkey,pkey,tkk)
    authstr = []
    
    with open("auth.txt","r") as authfile:
        authstr = authfile.readlines()
    while(True):
        try:
            wait4work = True
            while(wait4work):
                cur.execute('SELECT * FROM boombox.orders WHERE max24>=did24 AND done=0')
                myresult = cur.fetchone()
                if myresult != None:
                    print("found work to do so let's do it..")
                    wait4work = False
                else:
                    print("there's nothing to do so i'm goin to wait..")
                    time.sleep(60)

            warmup = True
            if(oner==False) or (authed is not ik):
                ok = sser+tric
            cprint("#"+str(round.value), "green")
            if(spmrunning == False):
                spmt.start()
                spmrunning = True
            pees = []
            give_him = []
            while len(give_him) < 1:
                try:
                    give_him = chunkIt(getacc1(),4)
                except:
                    cprint("Tokenserver is inresponsive, I'll wait..","yellow")
                    time.sleep(5)
            for i in range(4):
                try:
                    p = Process(target=pleaserunfortwohours, name='bitchnigga-'+str(i), args= (new, "y", give_him[i], i, q, autos, nautos, autof, nautof, ipmode, ipconf, plid, tpos, stop, follows, savess, realsent, round, 250,plen1,plen2,oout,percentage,rtime,authstr))
                    pees.append(p)
                    p.start()
                except Exception as e:
                    cprint(e,'yellow')
            time.sleep(63)
            print("terminating round 3.2.1..")
            for p in pees:
                p.terminate()
                p.join()
            round.value+=1
            gc.collect()
        except Exception as e:
            cprint(e,'red')
