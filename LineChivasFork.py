# -*- coding: utf-8 -*-
import LineAlpha
from LineAlpha.Gen.ttypes import *
from datetime import datetime
import time,random,sys,re,os,json,codecs,threading,glob,pytz

ka = LineAlpha.LINE()
ka.login(token="Token_Bot")
ka.loginResult()

kb = LineAlpha.LINE()
kb.login(token="Token_Bot")
kb.loginResult()

kc = LineAlpha.LINE()
kc.login(token="Token_Bot")
kc.loginResult()

kd = LineAlpha.LINE()
kd.login(token="Token_Bot")
kd.loginResult()

ke = LineAlpha.LINE()
ke.login(token="Token_Bot")
ke.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
╔═══[ Help ]
║𖤓≛≛≛≛≛≛𖤓
╠ Bot Menu
╠ Set Menu
╠ Group Menu
╠ Owner Menu
╠ Lurking on/off
╠ Lurking
╠ Lurking Reset
╠ Creator
╠ Tag/Tagall
║𖤓≛≛≛≛≛≛𖤓
╚═══[ Help ]
"""
helpGroup ="""
╔═══[ Help Group ]
║
║╔══════════
║╠ Ban
║╠ Gurl
║╠ Curl
║╠ Ourl
║╠ Clear
║╠ Ginfo
║╠ Unban
║╠ Banlist
║╠ Killban
║╚══════════
║
╚═══[ Help Group ]
"""

helpOwner ="""
╔═══[ Help Owner ]
║
║╔══════════
║╠ Set
║╠ 1/5invite 
║╠ Nk @ 
║╠ Cleanse
║╠ Keluar
║╠ Masuk
║╠ Admin Add @
║╠ Staff add @
║╠ Runtime
║╠ Bot restart
║╠ Remove all chat
║╚══════════
║
╚═══[ Help Owner ]
"""


helpBot =""" 
╔═══[ Help B O T ]
║
║╔══════════
║╠ Id
║╠ Me
║╠ Status
║╠ Speed 
║╠ Respon
║╠ All mid
║╠ Gift1/5
║╠ Stafflist
║╠ Adminlist
║╠ Ownerlist
║╚══════════
║
╚═══[ Help B O T ]
"""

helpSet =""" 
╔═══[ Help Setting ]
║
║╔══════════
║╠ Cancelinvite on/off
║╠ Cancel on/off
║╠ Qr on/off
║╠ Purge on/off 
║╠ Contact on/off
║╠ Join on/off
║╠ invite off
║╚══════════
║
╚═══[ Help Setting ]
"""
KAC=[ka,kb,kc,kd,ke]
mid = ka.getProfile().mid
Amid = kb.getProfile().mid
Bmid = kc.getProfile().mid
Cmid = kd.getProfile().mid
Dmid = ke.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid]
admin=["u3f2f024bfb418f735157dc53ea8ce64e"]
owner=["u3f2f024bfb418f735157dc53ea8ce64e"]
stafflist=["u3f2f024bfb418f735157dc53ea8ce64e"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "blacklist":{},
    "winvite" :False,
    "winvite2" :False,
    "winvite3" :False,
    "winvite4" :False,
    "winvite5" :False,
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "Protectjoin":True,
    "Protectcancl":True,
    "Protectcancel":True,
    "protectionOn":True,
    "atjointicket":True
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{}
}

setTime = {}
setTime = read['readTime']
mulai = time.time() 
#==============================================================================#
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
#==============================================================================#
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       ka.sendMessage(msg)
    except Exception as error:
       print error
#==============================================================================#
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)
#==============================================================================#
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
#==============================================================================#
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                ka.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    ka.sendText(op.param1,str(wait["message"]))
#==============================================================================#
        if op.type == 13:
          if mid in op.param3:
            if wait["autoJoin"] == True:
              if op.param2 in owner:
                ka.acceptGroupInvitation(op.param1)
                G = ka.getGroup(op.param1)
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                Ticket = ka.reissueGroupTicket(op.param1)
                kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                G.preventJoinByTicket = True
                ka.updateGroup(G)
              else:
                ka.rejectGroupInvitation(op.param1)
#==============================================================================#
          if Amid in op.param3:
            if wait["autoJoin"] == True:
              if op.param2 in owner:
                kb.acceptGroupInvitation(op.param1)
              else:
                kb.rejectGroupInvitation(op.param1)
            else:
              print "autoJoin is Off"
#==============================================================================#
          if Bmid in op.param3:
            if wait["autoJoin"] == True:
              if op.param2 in owner:
                kc.acceptGroupInvitation(op.param1)
              else:
                kc.rejectGroupInvitation(op.param1)
            else:
              print "autoJoin is Off"
#==============================================================================#
          if Cmid in op.param3:
            if wait["autoJoin"] == True:
              if op.param2 in owner:
                kd.acceptGroupInvitation(op.param1)
              else:
                kd.rejectGroupInvitation(op.param1)
            else:
              print "autoJoin is Off"
#==============================================================================#
          if Dmid in op.param3:
            if wait["autoJoin"] == True:
              if op.param2 in owner:
                ke.acceptGroupInvitation(op.param1)
              else:
                ke.rejectGroupInvitation(op.param1)
            else:
              print "autoJoin is Off"
#==============================================================================#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = ka.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 not in Bots or admin:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              else:
                try:
                  ka.cancelGroupInvitation(op.param1, gMembMids)
                  ka.sendText(op.param1,ka.getContact(op.param2).displayName + "\n" + "Who do you want to invite  ??? \nYou Are Not Our Admin, So We Cancel it.\nPlease Contact Admin/Owner")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                except:
                  random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "Who do you want to invite  ??? \nYou Are Not Our Admin, So We Cancel it.\nPlease Contact Admin/Owner")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#==============================================================================#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            if wait["blacklist"][op.param3] == True:
              ka.sendText(op.param1,ka.getContact(op.param3).displayName + " On Blacklist Boss\nWe Will Cancel Invitation")
              random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
#==============================================================================#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if ka.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              else:
                try:
                  ka.sendText(op.param1,ka.getContact(op.param2).displayName + "Dont Playing Link Group Bro")
                  ka.kickoutFromGroup(op.param1,[op.param2])
                  kb.kickoutFromGroup(op.param1,[op.param2])
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  kd.kickoutFromGroup(op.param1,[op.param2])
                  ke.kickoutFromGroup(op.param1,[op.param2])
                  ka.preventJoinByTicket = True
                  ka.sendText(op.param1,ka.getContact(op.param2).displayName + "\n" + "We Enter Into Blacklist Boss")
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Dont Playing Link Group Bro")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).preventJoinByTicket = True
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "We Enter Into Blacklist Boss")
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#==============================================================================#
        if op.type == 17: #Protect Join
          if wait["Protectjoin"] == True:
            if wait["blacklist"][op.param2] == True:
              ka.sendText(op.param1,ka.getContact(op.param2).displayName + " On Blacklist Boss\nWe Will Kick")
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            else:
              pass
#==============================================================================#
        if op.type == 19: #Member Ke Kick
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          else:
            try:
              ka.kickoutFromGroup(op.param1,[op.param2])
              kb.kickoutFromGroup(op.param1,[op.param2])
              kc.kickoutFromGroup(op.param1,[op.param2])
              kd.kickoutFromGroup(op.param1,[op.param2])
              ke.kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
            except:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
#==============================================================================#
        if op.type == 19:
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in Bots or owner:
                try:
                  G = kb.getGroup(op.param1)
                  kb.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kb.updateGroup(G)
                  Ticket = kb.reissueGroupTicket(op.param1)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kb.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kb.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#==============================================================================#
            elif op.param3 in Amid:
              if op.param2 not in Bots or owner:
                try:
                  G = kc.getGroup(op.param1)
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(op.param1)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kc.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Bmid:
              if op.param2 not in Bots or owner:
                try:
                  G = kd.getGroup(op.param1)
                  kd.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kd.updateGroup(G)
                  Ticket = kd.reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kd.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kd.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            elif op.param3 in Cmid:
              if op.param2 not in Bots or owner:
                try:
                  G = ke.getGroup(op.param1)
                  ke.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ke.updateGroup(G)
                  Ticket = ke.reissueGroupTicket(op.param1)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = ke.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ke.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            elif op.param3 in Dmid:
              if op.param2 not in Bots or owner:
                try:
                  G = ka.getGroup(op.param1)
                  ka.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ka.updateGroup(G)
                  Ticket = ka.reissueGroupTicket(op.param1)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = ka.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ka.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
        if op.type == 19: #admin dan stafflist
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in stafflist:
            pass
          else:
            try:
              if op.param3 in admin:
                if op.param2 not in Bots or owner:
                  if op.param2 in Bots:
                    pass
                  elif op.param2 in owner:
                    pass
                  else:
                    try:
                      ka.kickoutFromGroup(op.param1,[op.param2])
                      kb.kickoutFromGroup(op.param1,[op.param2])
                      kc.kickoutFromGroup(op.param1,[op.param2])
                      kd.kickoutFromGroup(op.param1,[op.param2])
                      ke.kickoutFromGroup(op.param1,[op.param2])
                      ka.inviteIntoGroup(op.param1,[op.param3])
                      kb.inviteIntoGroup(op.param1,[op.param3])
                      kc.inviteIntoGroup(op.param1,[op.param3])
                      kd.inviteIntoGroup(op.param1,[op.param3])
                      ke.inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).getGroup(op.param1)
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
#==============================================================================#
              elif op.param3 in stafflist:
                if op.param2 not in Bots or owner:
                  try:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                  except:
                    random.choice(KAC).getGroup(op.param1)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
            except:
              try:
                ka.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
#==============================================================================#
        if op.type == 22:
            if wait["leaveRoom"] == True:
                ka.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ka.leaveRoom(op.param1)
#==============================================================================#
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            ka.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = ka.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            ka.updateGroup(X)
                        except:
                            ka.sendText(msg.to,"error")
#==============================================================================#
        if op.type == 19:
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in stafflist:
            pass
          else:
            msg = Message(to=op.param1, from_=None, text=None, contentType=13)
            msg.contentMetadata={'mid':op.param2}
            ka.sendMessage(msg)
            ka.sendText(op.param1,ka.getContact(op.param2).displayName + " Kickers")
#==============================================================================#
        if op.type == 11:
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          elif op.param2 in stafflist:
            pass
          else:
            msg = Message(to=op.param1, from_=None, text=None, contentType=13)
            msg.contentMetadata={'mid':op.param2}
            ka.sendMessage(msg)
#==============================================================================#
        if op.type == 32:
          if wait["Protectcancel"] == True:
            if op.param2 not in admin:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in stafflist:
                pass
              else:
                random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + " Canceled Invitation")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                wait["blacklist"][op.param2] = True
#==============================================================================#
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    ka.leaveRoom(msg.to)
#==============================================================================#
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                ka.like(url[25:58], url[66:], likeType=1001)
                kb.like(url[25:58], url[66:], likeType=1002)
                kc.like(url[25:58], url[66:], likeType=1003)
                kd.like(url[25:58], url[66:], likeType=1004)
                ke.like(url[25:58], url[66:], likeType=1005)
#==============================================================================#
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
              if wait["winvite"] == True:
                if msg.from_ in admin:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = ka.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      ka.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      ka.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      ka.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        ka.findAndAddContactsByMid(target)
                        ka.inviteIntoGroup(msg.to,[target])
                        ka.sendText(msg.to,"Already Invited Boss 💋: \n➡" + _name)
                        wait["winvite"] = False
                        break
                      except:
                        try:
                          ka.findAndAddContactsByMid(invite)
                          ka.inviteIntoGroup(op.param1,[invite])
                          wait["winvite"] = False
                        except:
                          try:
                            ka.findAndAddContactsByMid(invite)
                            ka.inviteIntoGroup(op.param1,[invite])
                            wait["winvite"] = False
                            ka.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              ka.findAndAddContactsByMid(invite)
                              ka.inviteIntoGroup(op.param1,[invite])
                              wait["winvite"] = False
                              ka.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              ka.sendText(msg.to,"Negative, Error detected")
                              wait["winvite"] = False
                              break
              elif wait["winvite2"] == True:
                if msg.from_ in admin:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = kb.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      kb.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      kb.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      kb.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        kb.findAndAddContactsByMid(target)
                        kb.inviteIntoGroup(msg.to,[target])
                        kb.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite2"] = False
                        break
                      except:
                        try:
                          kb.findAndAddContactsByMid(invite)
                          kb.inviteIntoGroup(op.param1,[invite])
                          wait["winvite2"] = False
                        except:
                          try:
                            kb.findAndAddContactsByMid(invite)
                            kb.inviteIntoGroup(op.param1,[invite])
                            wait["winvite2"] = False
                            kb.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              kb.findAndAddContactsByMid(invite)
                              kb.inviteIntoGroup(op.param1,[invite])
                              wait["winvite2"] = False
                              kb.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              kb.sendText(msg.to,"Negative, Error detected")
                              wait["winvite2"] = False
                              break
              elif wait["winvite3"] == True:
                if msg.from_ in admin:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = kc.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      kc.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      kc.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      kc.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        kc.findAndAddContactsByMid(target)
                        kc.inviteIntoGroup(msg.to,[target])
                        kc.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite3"] = False
                        break
                      except:
                        try:
                          kc.findAndAddContactsByMid(invite)
                          kc.inviteIntoGroup(op.param1,[invite])
                          wait["winvite3"] = False
                        except:
                          try:
                            kc.findAndAddContactsByMid(invite)
                            kc.inviteIntoGroup(op.param1,[invite])
                            wait["winvite3"] = False
                            kc.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              kc.findAndAddContactsByMid(invite)
                              kc.inviteIntoGroup(op.param1,[invite])
                              wait["winvite3"] = False
                              kc.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              kc.sendText(msg.to,"Negative, Error detected")
                              wait["winvite3"] = False
                              break
              elif wait["winvite4"] == True:
                if msg.from_ in admin:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = kd.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      kd.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      kd.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      kd.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        kd.findAndAddContactsByMid(target)
                        kd.inviteIntoGroup(msg.to,[target])
                        kd.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite4"] = False
                        break
                      except:
                        try:
                          kd.findAndAddContactsByMid(invite)
                          kd.inviteIntoGroup(op.param1,[invite])
                          wait["winvite4"] = False
                        except:
                          try:
                            kd.findAndAddContactsByMid(invite)
                            kd.inviteIntoGroup(op.param1,[invite])
                            wait["winvite4"] = False
                            kd.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              kd.findAndAddContactsByMid(invite)
                              kd.inviteIntoGroup(op.param1,[invite])
                              wait["winvite4"] = False
                              kd.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              kd.sendText(msg.to,"Negative, Error detected")
                              wait["winvite4"] = False
                              break
              elif wait["winvite5"] == True:
                if msg.from_ in admin:
                  _name = msg.contentMetadata["displayName"]
                  invite = msg.contentMetadata["mid"]
                  groups = ke.getGroup(msg.to)
                  pending = groups.invitee
                  targets = []
                  for s in groups.members:
                    if _name in s.displayName:
                      ke.sendText(msg.to,"-> " + _name + " was here")
                      break
                    elif invite in wait["blacklist"]:
                      ke.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                      ke.sendText(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                      break
                    else:
                      targets.append(invite)
                  if targets == []:
                    pass
                  else:
                    for target in targets:
                      try:
                        ke.findAndAddContactsByMid(target)
                        ke.inviteIntoGroup(msg.to,[target])
                        ke.sendText(msg.to,"Already Invited Boss💋: \n➡" + _name)
                        wait["winvite5"] = False
                        break
                      except:
                        try:
                          ke.findAndAddContactsByMid(invite)
                          ke.inviteIntoGroup(op.param1,[invite])
                          wait["winvite5"] = False
                        except:
                          try:
                            ke.findAndAddContactsByMid(invite)
                            ke.inviteIntoGroup(op.param1,[invite])
                            wait["winvite5"] = False
                            ke.sendText(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                            break
                          except:
                            try:
                              ke.findAndAddContactsByMid(invite)
                              ke.inviteIntoGroup(op.param1,[invite])
                              wait["winvite5"] = False
                              ke.sendText(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                              break
                            except:
                              ke.sendText(msg.to,"Negative, Error detected")
                              wait["winvite5"] = False
                              break
#==============================================================================#
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        ka.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        ka.sendText(msg.to,"decided not to comment")
#==============================================================================#
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        ka.sendText(msg.to,"deleted")
                        wait["dblack"] = False
                   else:
                        wait["dblack"] = False
                        ka.sendText(msg.to,"It is not in the black list")
#==============================================================================#
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        ka.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ka.sendText(msg.to,"aded")
#==============================================================================#
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        ka.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False
                   else:
                        wait["dblacklist"] = False
                        ka.sendText(msg.to,"It is not in the black list")
#==============================================================================#
               elif wait["contact"] == True:
                    msg.contentType = 0
                    ka.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = ka.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ka.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ka.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = ka.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = ka.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        ka.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
#==============================================================================#
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    ka.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#==============================================================================#
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    ka.sendText(msg.to,helpMessage)
            elif msg.text in ["key group","Key Group","Group menu"]:
                if wait["lang"] == "JP":
                    ka.sendText(msg.to,helpGroup)
            elif msg.text in ["key set","Key Set","Set menu"]:
                if wait["lang"] == "JP":
                    ka.sendText(msg.to,helpSet)
            elif msg.text in ["key owner","Key Owner","Owner menu"]:
                if wait["lang"] == "JP":
                    ka.sendText(msg.to,helpOwner)
            elif msg.text in ["key bot","Key Bot","Bot menu"]:
                if wait["lang"] == "JP":
                    ka.sendText(msg.to,helpBot)
#==============================================================================#
            elif ("Gn " in msg.text):
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = ka.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    ka.updateGroup(X)
                else:
                    ka.sendText(msg.to,"It can't be used besides the group.")
#==============================================================================#
            elif "Kick " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Kick ","")
                ka.kickoutFromGroup(msg.to,[midd])
#==============================================================================#
            elif "Invite " in msg.text:
              if msg.from_ in owner:
                midd = msg.text.replace("Invite ","")
                ka.findAndAddContactsByMid(midd)
                ka.inviteIntoGroup(msg.to,[midd])
#==============================================================================#
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            ka.findAndAddContactsByMid(target)
                            kb.findAndAddContactsByMid(target)
                            kc.findAndAddContactsByMid(target)
                            kd.findAndAddContactsByMid(target)
                            ke.findAndAddContactsByMid(target)
                            admin.append(target)
                            ka.sendText(msg.to,"Admin Already Added Boss")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif "Owner add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Owner add executing"
                _name = msg.text.replace("Owner add @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            ka.findAndAddContactsByMid(target)
                            kb.findAndAddContactsByMid(target)
                            kc.findAndAddContactsByMid(target)
                            kd.findAndAddContactsByMid(target)
                            ke.findAndAddContactsByMid(target)
                            owner.append(target)
                            ka.sendText(msg.to,"Owner Already Added Boss")
                        except:
                            pass
                print "[Command]Owner add executed"
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            ka.sendText(msg.to,"Admin Deleted")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif "Owner remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Owner remove executing"
                _name = msg.text.replace("Owner remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            owner.remove(target)
                            ka.sendText(msg.to,"Owner Deleted")
                        except:
                            pass
                print "[Command]Owner remove executed"
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  ka.sendText(msg.to,"The stafflist is empty")
              else:
                  mc = "👑 Admin One Piece Bot 👑\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in admin:
                      mc += "[★]" + ka.getContact(mi_d).displayName + "\n"
                  ka.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
#==============================================================================#
            elif msg.text in ["Ownerlist","ownerlist"]:
              if owner == []:
                  ka.sendText(msg.to,"The Owner is empty")
              else:
                  mc = "👑 Owner One Piece Bot 👑\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in owner:
                      mc += "[★]" + ka.getContact(mi_d).displayName + "\n"
                  ka.sendText(msg.to,mc)
                  print "[Command]Ownerlist executed"
#==============================================================================#
            elif "Staff add @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Staff add @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   ka.sendText(msg.to,"Orang nya Ga Keliatan Kaya Setan")
                else:
                   for target in targets:
                        try:
                            ka.findAndAddContactsByMid(target)
                            kb.findAndAddContactsByMid(target)
                            kc.findAndAddContactsByMid(target)
                            kd.findAndAddContactsByMid(target)
                            ke.findAndAddContactsByMid(target)
                            stafflist.append(target)
                            ka.sendText(msg.to,"stafflist Already Added")
                        except:
                            pass
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif "Staff remove @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Staff remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   ka.sendText(msg.to,"Orangnya ga ada Lagi Colli")
                else:
                   for target in targets:
                        try:
                            stafflist.remove(target)
                            ka.sendText(msg.to,"stafflist Deleted")
                        except:
                            pass
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif msg.text in ["Stafflist","stafflist"]:
              if stafflist == []:
                  ka.sendText(msg.to,"stafflist nya Kosong Boss")
              else:
                  mc = "👥stafflist One Piece Team👥\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in stafflist:
                      mc += "👉 [★]" + ka.getContact(mi_d).displayName + "\n"
                  ka.sendText(msg.to,mc)
#==============================================================================#
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
#==============================================================================#
            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ka.sendMessage(msg)
#==============================================================================#
            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                kb.sendMessage(msg)
#==============================================================================#
            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kc.sendMessage(msg)
#==============================================================================#
            elif msg.text in ["Gift4"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kd.sendMessage(msg)
#==============================================================================#
            elif msg.text in ["Gift5"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                ke.sendMessage(msg)
#==============================================================================#
            elif msg.text in ["All gift"]:
              if msg.from_ in owner:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ka.sendMessage(msg)
                kb.sendMessage(msg)
                kc.sendMessage(msg)
                kd.sendMessage(msg)
                ke.sendMessage(msg)
#==============================================================================#
            elif msg.text in ["Ourl","Link on"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = ka.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Done")
                    else:
                        ka.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ka.sendText(msg.to,"Not for use less than group")
#==============================================================================#
            elif msg.text in ["Curl","Link off"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = ka.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Done")
                    else:
                        ka.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ka.sendText(msg.to,"Not for use less than group")
#==============================================================================#         
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = ka.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        ka.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        ka.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ka.sendText(msg.to,"Not for use less than group")
#==============================================================================#
            elif "Id" == msg.text:
                random.choice(KAC).sendText(msg.to,msg.to)
#==============================================================================#
            elif "All mid" == msg.text:
                ka.sendText(msg.to,mid)
                kb.sendText(msg.to,Amid)
                kc.sendText(msg.to,Bmid)
                kd.sendText(msg.to,Cmid)
                ke.sendText(msg.to,Dmid)
#==============================================================================#
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                random.choice(KAC).sendMessage(msg)
#==============================================================================#
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                ka.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+ka.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#==============================================================================#
            elif msg.text in ["Cancelinvite on","cancelinvite on"]:
              if msg.from_ in owner:
                if wait["Protectcancel"] == True:
                  if wait["lang"] == "JP":
                    ka.sendText(msg.to,"Protect Canceled Invited On")
                  else:
                    ka.sendText(msg.to,"Done")
                else:
                  wait["Protectcancel"] = True
                  if wait["lang"] == "JP":
                    ka.sendText(msg.to,"Protect Canceled Invited On")
                  else:
                    ka.sendText(msg.to,"done")
              else:
                ka.sendText(msg.to,"This Command Only For Owner")
#==============================================================================#
            elif msg.text in ["Cancelinvite off","cancelinvite off"]:
              if msg.from_ in owner:
                if wait["Protectcancel"] == False:
                  if wait["lang"] == "JP":
                    ka.sendText(msg.to,"Protect Canceled Invited Off")
                  else:
                    ka.sendText(msg.to,"Done")
                else:
                  wait["Protectcancel"] = False
                  if wait["lang"] == "JP":
                    ka.sendText(msg.to,"Protect Canceled Invited Off")
                  else:
                    ka.sendText(msg.to,"done")
              else:
                ka.sendText(msg.to,"This Command Only For Owner")
#==============================================================================#
            elif msg.text in ["Purge on","purge on","Purge: on","purge: on"]:
              if msg.from_ in owner:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"High Protect Activated")
                    else:
                        ka.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"High Protect Activated")
                    else:
                        ka.sendText(msg.to,"done")
              else:
                ka.sendText(msg.to,"This Command Only For Admin & Owner")
#==============================================================================#
            elif msg.text in ["Purge off","purge off","Purge: off","purge: off"]:
              if msg.from_ in owner:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"High Protect Disabled")
                    else:
                        ka.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"High Protect Disabled")
                    else:
                        ka.sendText(msg.to,"done")
              else:
                ka.sendText(msg.to,"This Command Only For Admin & Owner")
#==============================================================================#
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in owner:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Cancel All Invitation On")
                    else:
                        ka.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Cancel All Invitation On")
                    else:
                        ka.sendText(msg.to,"done")
              else:
                ka.sendText(msh.to, "This command only for owner")
#==============================================================================#
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in owner:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Cancel All Invitation Off")
                    else:
                        ka.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Cancel All Invitation Off")
                    else:
                        ka.sendText(msg.to,"done")
              else:
                ka.sendText(msh.to, "This command only for owner")
#==============================================================================#
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in owner:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Protect QR On")
                    else:
                        ka.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Protect QR On")
                    else:
                        ka.sendText(msg.to,"done")
              else:
                ka.sendText(msh.to, "This command only for owner")
#==============================================================================#
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in owner:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Protect QR Off")
                    else:
                        ka.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Protect QR Off")
                    else:
                        ka.sendText(msg.to,"done")
              else:
                ka.sendText(msh.to, "This command only for owner")
#==============================================================================#
            elif msg.text in ["Invite off","invite off"]:
              if msg.from_ in owner:
                if wait["winvite"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Dibatalin")
                    else:
                        ka.sendText(msg.to,"Dibatalin")
                else:
                    wait["winvite"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Dibatalin")
                    else:
                        ka.sendText(msg.to,"Dibatalin")
#==============================================================================#
                if wait["winvite2"] == False:
                    if wait["lang"] == "JP":
                        kb.sendText(msg.to,"Dibatalin")
                    else:
                        kb.sendText(msg.to,"Dibatalin")
                else:
                    wait["winvite2"] = False
                    if wait["lang"] == "JP":
                        kb.sendText(msg.to,"Dibatalin")
                    else:
                        kb.sendText(msg.to,"Dibatalin")
#==============================================================================#
                if wait["winvite3"] == False:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Dibatalin")
                    else:
                        kc.sendText(msg.to,"Dibatalin")
                else:
                    wait["winvite3"] = False
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Dibatalin")
                    else:
                        kc.sendText(msg.to,"Dibatalin")
#==============================================================================#
            elif msg.text in ["Contact on"]:
              if msg.from_ in owner:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Info Contact")
                    else:
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Info Contact")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Info Contact")
                    else:
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Info Contact")
#==============================================================================#
            elif msg.text in ["Contact off"]:
              if msg.from_ in owner:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Info Contact")
                    else:
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Info Contact")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Info Contact")
                    else:
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Info Contact")
#==============================================================================#
            elif msg.text in ["Join on"]:
              if msg.from_ in owner:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Auto Join")
                    else:
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Auto Join")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Auto Join")
                    else:
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Auto Join")
#==============================================================================#
            elif msg.text in ["Join off"]:
              if msg.from_ in owner:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Auto Join")
                    else:
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Auto Join")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Auto Join")
                    else:
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Auto Join")
#==============================================================================#
            elif msg.text in ["Leave on"]:
              if msg.from_ in owner:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Auto Leave")
                    else:
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Auto Leave")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Auto Leave")
                    else:
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Auto Leave")
#==============================================================================#
            elif msg.text in ["Leave off"]:
              if msg.from_ in owner:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Auto Leave")
                    else:
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Auto Leave")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Auto Leave")
                    else:
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Auto Leave")
#==============================================================================#
            elif msg.text in ["Share on"]:
              if msg.from_ in owner:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Share")
                    else:
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Share")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Share")
                    else:
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Share")
#==============================================================================#
            elif msg.text in ["Share off"]:
              if msg.from_ in owner:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Share")
                    else:
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Share")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Share")
                    else:
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Share")
#==============================================================================#
            elif msg.text in ["Set"]:
              if msg.from_ in owner:
                md = ""
                if wait["contact"] == True: md+=" Contact : on\n"
                else: md+=" Contact : off\n"
                if wait["Protectgr"] == True: md+=" Protect Qr : on\n"
                else: md+=" Protect Qr : off\n"
                if wait["Protectcancl"] == True: md+=" Cancel : on\n"
                else: md+=" Cancel : off\n"
                if wait["Protectcancel"] == True: md+=" Cancelinvite : on\n"
                else: md+=" Cancelinvite : off\n"
                if wait["Protectjoin"] == True: md+=" Purge : on\n"
                else: md+=" Purge : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share : on\n"
                else:md+=" Share : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                ka.sendText(msg.to,md)
#==============================================================================#
            elif "Album merit " in msg.text:
                gid = msg.text.replace("Album merit ","")
                album = ka.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Tidak Ada Album")
                    else:
                        ka.sendText(msg.to,"Tidak Ada Album")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album target"
                    else:
                        mg = "Berikut ini adalah album target"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    ka.sendText(msg.to,mg)
#==============================================================================#
            elif "Album " in msg.text:
                gid = msg.text.replace("Album ","")
                album = ka.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Tidak Ada Album")
                    else:
                        ka.sendText(msg.to,"Tidak Ada Album")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album target"
                    else:
                        mg = "Berikut ini adalah album target"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
#==============================================================================#
            elif msg.text in ["Group id"]:
              if msg.from_ in owner:
                gid = ka.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (ka.getGroup(i).name,i)
                ka.sendText(msg.to,h)
#==============================================================================#
            elif "Album remove" in msg.text:
                gid = msg.text.replace("album remove","")
                albums = ka.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        ka.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    ka.sendText(msg.to,str(i) + "Albums Deleted")
                else:
                    ka.sendText(msg.to,str(i) + "Albums Deleted")
#==============================================================================#
            elif msg.text in ["Autoadd on"]:
              if msg.from_ in owner:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Auto Add")
                    else:
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Auto Add")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Auto Add")
                    else:
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Auto Add")
#==============================================================================#
            elif msg.text in ["Autoadd off"]:
              if msg.from_ in owner:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Auto Add")
                    else:
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Auto Add")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Auto Add")
                    else:
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Auto Add")
#==============================================================================#
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                ka.sendText(msg.to,"Pesan Dirubah")
#==============================================================================#
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    ka.sendText(msg.to,"Pesan Dirubah")
                else:
                    ka.sendText(msg.to,"Pesan Dirubah")
#==============================================================================#
            elif msg.text in ["Message"]:
                if wait["lang"] == "JP":
                    ka.sendText(msg.to,"Pesan Berubah Menjadi\n\n" + wait["message"])
                else:
                    ka.sendText(msg.to,"Informasi Penambahan Otomatis Diatur Sebagai Berikut\n\n" + wait["message"])
#==============================================================================#
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    ka.sendText(msg.to,"Pesan Dirubah")
                else:
                    wait["comment"] = c
                    ka.sendText(msg.to,"changed\n\n" + c)
#==============================================================================#
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    ka.sendText(msg.to,"Tidak Bisa Dirubah")
                else:
                    wait["comment"] = c
                    ka.sendText(msg.to,"changed\n\n" + c)
#==============================================================================#
            elif msg.text in ["Comment on"]:
              if msg.from_ in owner:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Comment")
                    else:
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Comment")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Comment")
                    else:
                        ka.sendText(msg.to,"Berhasil Mengaktifkan Comment")
#==============================================================================#
            elif msg.text in ["Comment off"]:
              if msg.from_ in owner:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Comment")
                    else:
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Comment")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Comment")
                    else:
                        ka.sendText(msg.to,"Berhasil Menonaktifkan Comment")
#==============================================================================#
            elif msg.text in ["Comment"]:
                ka.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
#==============================================================================#
            elif msg.text in ["Gurl"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    x = ka.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ka.updateGroup(x)
                    gurl = ka.reissueGroupTicket(msg.to)
                    ka.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Tidak bisa digunakan diluar kelompok")
                    else:
                        ka.sendText(msg.to,"Tidak untuk penggunaan kurang dari kelompok")
#==============================================================================#
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                ka.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                ka.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    ka.sendText(msg.to,"confirmed")
                else:
                    ka.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +ka.getContact(mi_d).displayName + "\n"
                    ka.sendText(msg.to,mc)
#==============================================================================#
            elif msg.text in ["Tag"]:
                group = ka.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                  summon(msg.to, nama)
                if jml > 100 and jml < 200:
                  for i in range(0, 99):
                    nm1 += [nama[i]]
                  summon(msg.to, nm1)
                  for j in range(100, len(nama)-1):
                    nm2 += [nama[j]]
                  summon(msg.to, nm2)
                if jml > 200  and jml < 500:
                  for i in range(0, 99):
                    nm1 += [nama[i]]
                  summon(msg.to, nm1)
                  for j in range(100, 199):
                    nm2 += [nama[j]]
                  summon(msg.to, nm2)
                  for k in range(200, 299):
                    nm3 += [nama[k]]
                  summon(msg.to, nm3)
                  for l in range(300, 399):
                    nm4 += [nama[l]]
                  summon(msg.to, nm4)
                  for m in range(400, len(nama)-1):
                    nm5 += [nama[m]]
                  summon(msg.to, nm5)
                if jml > 500:
                  print "Terlalu Banyak Men 500+"
                cnt = Message()
                cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                cnt.to = msg.to
                ka.sendMessage(cnt)
#==============================================================================#
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                ka.sendText(msg.to,van)
#==============================================================================#
            elif msg.text in ["Remove all chat"]:
              if msg.from_ in owner:
                ka.sendText(msg.to,"Starting Remove All Chat...")
                ka.removeAllMessages(op.param2)
                kb.removeAllMessages(op.param2)
                kc.removeAllMessages(op.param2)
                kd.removeAllMessages(op.param2)
                ke.removeAllMessages(op.param2)
                ka.sendText(msg.to,"All Chat In Bots Removed")
#==============================================================================#
            elif msg.text == "Lurking on":
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                hr = timeNow.strftime("%A")
                bln = timeNow.strftime("%m")
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                if msg.to in read['readPoint']:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            ka.sendText(msg.to,"Lurking already on")
                else:
                    try:
                        del read['readPoint'][msg.to]
                        del read['readMember'][msg.to]
                        del read['readTime'][msg.to]
                    except:
                        pass
                    read['readPoint'][msg.to] = msg.id
                    read['readMember'][msg.to] = ""
                    read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    read['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                        json.dump(read, fp, sort_keys=True, indent=4)
                        ka.sendText(msg.to, "Set reading point:\n" + readTime)
#==============================================================================#
            elif msg.text == "Lurking off":
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                hr = timeNow.strftime("%A")
                bln = timeNow.strftime("%m")
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                if msg.to not in read['readPoint']:
                    ka.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                    except:
                          pass
                    ka.sendText(msg.to, "Delete reading point:\n" + readTime)
#==============================================================================#
            elif msg.text == "Lurking reset":
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                hr = timeNow.strftime("%A")
                bln = timeNow.strftime("%m")
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                if msg.to in read["readPoint"]:
                    try:
                        read["readPoint"][msg.to] = True
                        read["readMember"][msg.to] = {}
                        read["readTime"][msg.to] = readTime
                        read["ROM"][msg.to] = {}
                    except:
                        pass
                    ka.sendText(msg.to, "Reset reading point:\n" + readTime)
                else:
                    ka.sendText(msg.to, "Lurking belum diaktifkan ngapain di reset?")
#==============================================================================#          
            elif msg.text == "Lurking":
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                        if read["ROM"][msg.to].items() == []:
                             ka.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][msg.to].items():
                                chiya.append(rom[1])
                                   
                            cmem = ka.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
                        msg.text = xpesan+ zxc + "\nLurking time: \n" + readTime
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        msg.contentMetadata = lol
                        try:
                          ka.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
                    else:
                        ka.sendText(msg.to, "Lurking has not been set.")
#==============================================================================#
            elif msg.text in ["Masuk"]:
              if msg.from_ in owner:
                        G = ka.getGroup(msg.to)
                        ginfo = ka.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        ka.updateGroup(G)
                        invsend = 0
                        Ticket = ka.reissueGroupTicket(msg.to)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = ka.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ka.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ka.updateGroup(G)
#==============================================================================#
            elif msg.text in ["Keluar"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = ka.getGroup(msg.to)
                    try:
                        kb.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                    except:
                        pass
#==============================================================================#
            elif msg.text in ["Bot restart"]:
              if msg.from_ in owner:
    	          ka.sendText(msg.to, "Kami Siap Restart\nWaktu Restart Sekitar 10 Detik ")
                  restart_program()
              else:
                ka.sendText(msg.to,"This Command Only For Owner")
#==============================================================================#
            elif "Cleanse" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Cleanse","")
                    gs = ka.getGroup(msg.to)
                    gs = kb.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    ka.sendText(msg.to,"Just Some Casual Cleansing ")
                    ka.sendText(msg.to,"Group Cleansed")
                    ka.sendText(msg.to,"Fuck You All")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ka.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[ka,kb,kc,kd,ke]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ka.sendText(msg.to,"Group cleanse")
#==============================================================================#
            elif "Nk " in msg.text:
              if msg.from_ in owner:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ka.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"Pengguna Tidak Ada")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[ka,kb,kc,kd,ke]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ka.sendText(msg.to,"Mohon Maaf Kawan")
                                    ka.sendText(msg.to,"😭")
#==============================================================================#
            elif msg.text in ["Test"]:
                ka.sendText(msg.to,"Ok double thumbs up􏿿")
                kb.sendText(msg.to,"Ok double thumbs up􏿿")
                kc.sendText(msg.to,"Ok double thumbs up􏿿")
                kd.sendText(msg.to,"Ok double thumbs up􏿿")
                ke.sendText(msg.to,"Ok double thumbs up􏿿")
#==============================================================================#
            elif "Bc " in msg.text:
              if msg.from_ in owner:
				bctxt = msg.text.replace("Bc ","")
				ka.sendText(msg.to,(bctxt))
#==============================================================================#
            elif msg.text in ["Hai","hai"]:
                ka.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kb.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kd.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ke.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
#==============================================================================#
            elif msg.text in ["Welcome"]:
                ka.sendText(msg.to,"Selamat datang di Chivas Family Room")
                ka.sendText(msg.to,"Jangan nakal ok!")
#==============================================================================#
            elif msg.text in ["PING","Ping","ping"]:
                ka.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kb.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kd.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ke.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#==============================================================================#
            elif msg.text in ["Respon","respon"]:
                ka.sendText(msg.to,"Hadir")
                kb.sendText(msg.to,"Hadir")
                kc.sendText(msg.to,"Hadir")
                kd.sendText(msg.to,"Hadir")
                ke.sendText(msg.to,"Hadir")
#==============================================================================#
            elif msg.text in ["1invite"]:
              if msg.from_ in owner:
                wait["winvite"] = True
                ka.sendText(msg.to,"Share contact boss 😎")
#==============================================================================#
            elif msg.text in ["2invite"]:
              if msg.from_ in owner:
                wait["winvite2"] = True
                kb.sendText(msg.to,"Share contact boss 😎")
#==============================================================================#
            elif msg.text in ["3invite"]:
              if msg.from_ in owner:
                wait["winvite3"] = True
                kc.sendText(msg.to,"Share contact boss 😎")
#==============================================================================#
            elif msg.text in ["4invite"]:
              if msg.from_ in owner:
                wait["winvite4"] = True
                kd.sendText(msg.to,"Share contact boss 😎")
#==============================================================================#
            elif msg.text in ["5invite"]:
              if msg.from_ in owner:
                wait["winvite5"] = True
                ke.sendText(msg.to,"Share contact boss 😎")
#==============================================================================#
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                ka.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                ka.sendText(msg.to, "%sseconds" % (elapsed_time))
#==============================================================================#
            elif msg.text in ["Ban"]:
              if msg.from_ in owner:
                wait["wblacklist"] = True
                ka.sendText(msg.to,"Send Contact")
#==============================================================================#
            elif msg.text in ["Unban"]:
              if msg.from_ in owner:
                wait["dblacklist"] = True
                ka.sendText(msg.to,"Send Contact")
#==============================================================================#
            elif msg.text in ["Creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'u3f2f024bfb418f735157dc53ea8ce64e'}
              ka.sendMessage(msg)
#==============================================================================#
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    ka.sendText(msg.to,"Tidak Ada Daftar Blacklist")
                else:
                    ka.sendText(msg.to,"Daftar Blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "▶" +ka.getContact(mi_d).displayName + "\n"
                    ka.sendText(msg.to,mc)
#==============================================================================#
            elif msg.text in ["Killban"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Tidak Ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"Blacklist Memang Pantas Untuk Di Usir")
#==============================================================================#
            elif msg.text in ["Clear"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
                    random.choice(KAC).sendText(msg.to,"Berhasil Membatalkan Semua Undangan.")
#==============================================================================#
            elif "Random" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = ka.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            ka.updateGroup(group)
                    except:
                        ka.sendText(msg.to,"Error")
#==============================================================================#
            elif "Albumat" in msg.text:
                try:
                    albumtags = msg.text.replace("Albumat","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    ka.createAlbum(gid,name)
                    ka.sendText(msg.to,name + "created an album")
                except:
                    ka.sendText(msg.to,"Error")
#==============================================================================#
            elif "Fakecat" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("Fakecat","")
                    ka.sendText(msg.to,str(ka.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        ka.sendText(msg.to,str(e))
                    except:
                        pass
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
           
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                        json.dump(read, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass 
            
#==============================================================================#
    except Exception as error:
        print error
#==============================================================================#
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
#==============================================================================#
while True:
    try:
        Ops = ka.fetchOps(ka.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(ka.Poll.rev))
#==============================================================================#
    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            ka.Poll.rev = max(ka.Poll.rev, Op.revision)
            bot(Op)
#==============================================================================#