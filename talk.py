# -*- coding: utf-8 -*-
from line_relation.ttypes import *
from akad.ttypes import Message, Location, DeleteOtherFromChatRequest, RejectChatInvitationRequest, CancelChatInvitationRequest, InviteIntoChatRequest, CreateChatRequest, UpdateChatRequest, GetChatsRequest, FindChatByTicketRequest, ReissueChatTicketRequest, AcceptChatInvitationByTicketRequest, AcceptChatInvitationRequest, GetAllChatMidsRequest, DeleteSelfFromChatRequest, GetInvitationTicketUrlRequest
from random import randint
from bs4 import BeautifulSoup

import json, ntpath
import requests

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to LINE')
    return checkLogin

class Talk(object):
    isLogin = False
    _messageReq = {}
    _unsendMessageReq = 0

    def __init__(self):
        self.isLogin = True

    """Group"""
    @loggedIn
    def deleteOtherFromChat(self, chatMid, targetUserMids=[]):
        return self.talk.deleteOtherFromChat(DeleteOtherFromChatRequest(0,chatMid,targetUserMids))
        
    @loggedIn
    def inviteIntoChat(self, chatMid, targetUserMids=[]):
        return self.talk.inviteIntoChat(InviteIntoChatRequest(0,chatMid,targetUserMids))
     
    @loggedIn
    def acceptChatInvitation(self, chatMid):
        return self.talk.acceptChatInvitation(AcceptChatInvitationRequest(0,chatMid))

    @loggedIn
    def cancelChatInvitation(self, chatMid, targetUserMids=[]):
        return self.talk.cancelChatInvitation(CancelChatInvitationRequest(0,chatMid,targetUserMids))

    @loggedIn
    def createChat(self, name, targetUserMids=[]):
        return self.talk.createChat(CreateChatRequest(0,0,name,targetUserMids,""))
       
    @loggedIn
    def getAllChatMids(self, withMemberChats=True, withInvitedChats=True):
        return self.talk.getAllChatMids(GetAllChatMidsRequest(withMemberChats,withInvitedChats), 0)
        
    @loggedIn
    def deleteSelfFromChat(self,chatMid):
        req = DeleteSelfFromChatRequest()
        req.reqSeq = 0
        req.chatMid = chatMid
        return self.talk.deleteSelfFromChat(req)

    @loggedIn
    def getInvitationTicketUrl(self, mid):
        return self.talk.getInvitationTicketUrl(GetInvitationTicketUrlRequest(mid))
    
    @loggedIn
    def rejectChatInvitation(self, chatMid):
        return self.talk.rejectChatInvitation(RejectChatInvitationRequest(0,chatMid))

    @loggedIn
    def acceptChatInvitationByTicket(self, chatMid, ticketId):
        return self.talk.acceptChatInvitationByTicket(AcceptChatInvitationByTicketRequest(0,chatMid,ticketId))

    @loggedIn
    def reissueChatTicket(self, chatMid):
        return self.talk.reissueChatTicket(ReissueChatTicketRequest(0,chatMid))

    @loggedIn
    def findChatByTicket(self, ticketId):
        return self.talk.findChatByTicket(FindChatByTicketRequest(ticketId))

    @loggedIn
    def getChats(self, chatMids=[], withMembers=True, withInvitees=True):
        return self.talk.getChats(GetChatsRequest(chatMids,withMembers,withInvitees))
    
    @loggedIn
    def updateChat(self, chat, updatedAttribute):
        return self.talk.updateChat(UpdateChatRequest(0,chat,updatedAttribute))
        
    @loggedIn
    def getChatRoomAnnouncementsBulk(self, chatRoomMids):
        return self.talk.getChatRoomAnnouncementsBulk(chatRoomMids)

    @loggedIn
    def getChatRoomAnnouncements(self, chatRoomMid):
        return self.talk.getChatRoomAnnouncements(chatRoomMid)

    @loggedIn
    def createChatRoomAnnouncement(self, chatRoomMid, type, contents):
        return self.talk.createChatRoomAnnouncement(0, chatRoomMid, type, contents)

    @loggedIn
    def removeChatRoomAnnouncement(self, chatRoomMid, announcementSeq):
        return self.talk.removeChatRoomAnnouncement(0, chatRoomMid, announcementSeq)

    @loggedIn
    def getGroupWithoutMembers(self, groupId):
        return self.talk.getGroupWithoutMembers(groupId)
    
    @loggedIn
    def findGroupByTicket(self, ticketId):
        return self.talk.findGroupByTicket(ticketId)

    @loggedIn
    def acceptGroupInvitation(self, groupId):
        return self.talk.acceptGroupInvitation(0, groupId)

    @loggedIn
    def acceptGroupInvitationByTicket(self, groupId, ticketId):
        return self.talk.acceptGroupInvitationByTicket(0, groupId, ticketId)

    @loggedIn
    def cancelGroupInvitation(self, groupId, contactIds):
        return self.talk.cancelGroupInvitation(0, groupId, contactIds)

    @loggedIn
    def createGroup(self, name, midlist):
        return self.talk.createGroup(0, name, midlist)

    @loggedIn
    def getGroup(self, groupId):
        return self.talk.getGroup(groupId)

    @loggedIn
    def getGroups(self, groupIds):
        return self.talk.getGroups(groupIds)

    @loggedIn
    def getGroupsV2(self, groupIds):
        return self.talk.getGroupsV2(groupIds)

    @loggedIn
    def getCompactGroup(self, groupId):
        return self.talk.getCompactGroup(groupId)

    @loggedIn
    def getCompactRoom(self, roomId):
        return self.talk.getCompactRoom(roomId)

    @loggedIn
    def getGroupIdsByName(self, groupName):
        gIds = []
        for gId in self.getGroupIdsJoined():
            g = self.getCompactGroup(gId)
            if groupName in g.name:
                gIds.append(gId)
        return gIds

    @loggedIn
    def getGroupIdsInvited(self):
        return self.talk.getGroupIdsInvited()

    @loggedIn
    def getGroupIdsJoined(self):
        return self.talk.getGroupIdsJoined()

    @loggedIn
    def updateGroupPreferenceAttribute(self, groupMid, updatedAttrs):
        return self.talk.updateGroupPreferenceAttribute(0, groupMid, updatedAttrs)

    @loggedIn
    def inviteIntoGroup(self, groupId, midlist):
        return self.talk.inviteIntoGroup(0, groupId, midlist)

    @loggedIn
    def kickoutFromGroup(self, groupId, midlist):
        return self.talk.kickoutFromGroup(0, groupId, midlist)

    @loggedIn
    def leaveGroup(self, groupId):
        return self.talk.leaveGroup(0, groupId)

    @loggedIn
    def rejectGroupInvitation(self, groupId):
        return self.talk.rejectGroupInvitation(0, groupId)

    @loggedIn
    def reissueGroupTicket(self, groupId):
        return self.talk.reissueGroupTicket(groupId)

    @loggedIn
    def updateGroup(self, groupObject):
        return self.talk.updateGroup(0, groupObject)

    """User"""

    @loggedIn
    def acquireEncryptedAccessToken(self, featureType=2):
        return self.talk.acquireEncryptedAccessToken(featureType)

    @loggedIn
    def getProfile(self):
        return self.talk.getProfile()

    @loggedIn
    def getSettings(self):
        return self.talk.getSettings()

    @loggedIn
    def getUserTicket(self):
        return self.talk.getUserTicket()
        
        
        
    @loggedIn
    def sendMentionV2(self, to, text="", mids=[], isUnicode=False):
        arrData = ""
        arr = []
        mention = "@BEN "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ""
            unicode = ""
            if isUnicode:
                for mid in mids:
                    unicode += str(texts[mids.index(mid)].encode('unicode-escape'))
                    textx += str(texts[mids.index(mid)])
                    slen = len(textx) if unicode == textx else len(textx) + unicode.count('U0')
                    elen = len(textx) + 8
                    arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                    arr.append(arrData)
                    textx += mention
            else:
                for mid in mids:
                    textx += str(texts[mids.index(mid)])
                    slen = len(textx)
                    elen = len(textx) + 8
                    arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                    arr.append(arrData)
                    textx += mention
            textx += str(texts[len(mids)])
        else:
            raise Exception("Invalid mention position")
        self.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

    @loggedIn
    def generateUserTicket(self):
        try:
            ticket = self.getUserTicket().id
        except:
            self.reissueUserTicket()
            ticket = self.getUserTicket().id
        return ticket

    @loggedIn
    def updateProfile(self, profileObject):
        return self.talk.updateProfile(0, profileObject)

    @loggedIn
    def updateSettings(self, settingObject):
        return self.talk.updateSettings(0, settingObject)

    @loggedIn
    def updateProfileAttribute(self, attrId, value):
        return self.talk.updateProfileAttribute(0, attrId, value)

    @loggedIn
    def updateContactSetting(self, mid, flag, value):
        return self.talk.updateContactSetting(0, mid, flag, value)

    @loggedIn
    def deleteContact(self, mid):
        return self.updateContactSetting(mid, 16, 'True')

    @loggedIn
    def renameContact(self, mid, name):
        return self.updateContactSetting(mid, 2, name)

    @loggedIn
    def addToFavoriteContactMids(self, mid):
        return self.updateContactSetting(mid, 8, 'True')

    @loggedIn
    def addToHiddenContactMids(self, mid):
        return self.updateContactSetting(mid, 4, 'True')

    """Operation"""

    @loggedIn
    def fetchOps(self, localRev, count, globalRev=0, individualRev=0):
        return self.poll.fetchOps(self, localRev, count, globalRev, individualRev)

    @loggedIn
    def fetchOperation(self, revision, count=1):
        return self.poll.fetchOperations(revision, count)

    @loggedIn
    def getLastOpRevision(self):
        return self.poll.getLastOpRevision()

    """Message"""

    @loggedIn
    def sendMessage(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)
        
    @loggedIn
    def getRecentMessagesV2(self, chatId, count=1001):
        return self.talk.getRecentMessagesV2(chatId,count)

    @loggedIn
    def sendMessageObject(self, msg):
        to = msg.to
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        self._msgReq += 1
        return self.talk.sendMessage(self._messageReq[to], msg)

    @loggedIn
    def sendLocation(self, to, address, latitude, longitude, phone=None, contentMetadata={}):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = "Location by Hello World"
        msg.contentType, msg.contentMetadata = 0, contentMetadata
        location = Location()
        location.address = address
        location.phone = phone
        location.latitude = float(latitude)
        location.longitude = float(longitude)
        location.title = "Location"
        msg.location = location
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)

    @loggedIn
    def sendMusic(self, to, title=None, subText=None, url=None, iconurl=None, contentMetadata={}):
        """
        a : Android
        i : Ios
        """
        self.profile = self.getProfile()
        self.userTicket = self.generateUserTicket()
        title = title if title else 'LINE MUSIC'
        subText = subText if subText else self.profile.displayName
        url = url if url else 'line://ti/p/' + self.userTicket
        iconurl = iconurl if iconurl else 'https://obs.line-apps.com/os/p/%s' % self.profile.mid
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = title
        msg.contentType = 19
        msg.contentMetadata = {
            'text': title,
            'subText': subText,
            'a-installUrl': url,
            'i-installUrl': url,
            'a-linkUri': url,
            'i-linkUri': url,
            'linkUri': url,
            'previewUrl': iconurl,
            'type': 'mt',
            'a-packageName': 'com.spotify.music',
            'countryCode': 'JP',
            'id': 'mt000000000a6b79f9'
        }
        if contentMetadata:
            msg.contentMetadata.update(contentMetadata)
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)

    @loggedIn
    def generateMessageFooter(self, title=None, link=None, iconlink=None):
        self.profile = self.getProfile()
        self.userTicket = self.generateUserTicket()
        title = title if title else self.profile.displayName
        link = link if link else 'line://ti/p/' + self.userTicket
        iconlink = iconlink if iconlink else 'https://obs.line-apps.com/os/p/%s' % self.profile.mid
        return {'AGENT_NAME': title, 'AGENT_LINK': link, 'AGENT_ICON': iconlink}

    @loggedIn
    def sendMessageWithFooter(self, to, text, title=None, link=None, iconlink=None, contentMetadata={}):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType = 0
        msg.contentMetadata = self.generateMessageFooter(title, link, iconlink)
        if contentMetadata:
            msg.contentMetadata.update(contentMetadata)
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)

    @loggedIn
    def generateReplyMessage(self, relatedMessageId):
        msg = Message()
        msg.relatedMessageServiceCode = 1
        msg.messageRelationType = 3
        msg.relatedMessageId = str(relatedMessageId)
        return msg

    @loggedIn
    def sendReplyMessage(self, relatedMessageId, to, text, contentMetadata={}, contentType=0):
        msg = self.generateReplyMessage(relatedMessageId)
        msg.to = to
        msg.text = text
        msg.contentType = contentType
        msg.contentMetadata = contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)
        
    @loggedIn
    def createEmail(self, sep1, sep2):
        url   = 'https://api.boteater.vip/email?email=%s&pass=%s' % (sep1,sep2)
        get   = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        bss   = BeautifulSoup(get.text, 'lxml')
        isi   = bss.find('p')
        res   = isi.get_text()
        res   = str(res)
        web   = res.split('WEBMAIL:')[1]
        ret_  = 'Email Generate'
        ret_ += '\nEmail    : %s@boteater.vip' % sep1
        ret_ += '\nPassword : %s' % sep2
        ret_ += '\nWebmail  : %s' % web
        ret_ += '\n[JTB]'
        return ret_

    """ Usage:
        @to Integer
        @text String
        @dataMid List of user Mid
    """
    @loggedIn
    def sendMessageWithMention(self, to, text='', dataMid=[]):
        arr = []
        list_text=''
        if '[list]' in text.lower():
            i=0
            for l in dataMid:
                list_text+='\n@[list-'+str(i)+']'
                i=i+1
            text=text.replace('[list]', list_text)
        elif '[list-' in text.lower():
            text=text
        else:
            i=0
            for l in dataMid:
                list_text+=' @[list-'+str(i)+']'
                i=i+1
            text=text+list_text
        i=0
        for l in dataMid:
            mid=l
            name='@[list-'+str(i)+']'
            ln_text=text.replace('\n',' ')
            if ln_text.find(name):
                line_s=int(ln_text.index(name))
                line_e=(int(line_s)+int(len(name)))
            arrData={'S': str(line_s), 'E': str(line_e), 'M': mid}
            arr.append(arrData)
            i=i+1
        contentMetadata={'MENTION':str('{"MENTIONEES":' + json.dumps(arr).replace(' ','') + '}')}
        return self.sendMessage(to, text, contentMetadata)
        
    @loggedIn
    def sendFooter(self, to, text, agentIcon, agentName, agentLink):
        contentMetadata = {
            'AGENT_ICON': agentIcon,
            'AGENT_NAME': agentName,
            'AGENT_LINK': agentLink
        }
        return self.sendMessage(to, text, contentMetadata, 0)

    @loggedIn
    def sendSticker(self, to, packageId, stickerId):
        contentMetadata = {
            'STKVER': '100',
            'STKPKGID': packageId,
            'STKID': stickerId
        }
        return self.sendMessage(to, '', contentMetadata, 7)
        
    @loggedIn
    def sendContact(self, to, mid):
        contentMetadata = {'mid': mid}
        return self.sendMessage(to, '', contentMetadata, 13)
        
    @loggedIn
    def sendContactHP(self, to, text, nomer, nama):
        nomer = nomer
        nama = nama
        contentMetadata = {
            'vCard': 'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:ANDROID 8.13.3 Android OS 4.4.4\r\nFN:\\{}\r\nTEL;TYPE=mobile:{}\r\nN:?;\\,\r\nEND:VCARD\r\n'.format(nama,nomer),
            'displayName': '{}'.format(nama)
        }
        return self.sendMessage(to, text, contentMetadata, 13)

    @loggedIn
    def sendGift(self, to, productId, productType):
        if productType not in ['theme','sticker']:
            raise Exception('Invalid productType value')
        contentMetadata = {
            'MSGTPL': str(randint(0, 12)),
            'PRDTYPE': productType.upper(),
            'STKPKGID' if productType == 'sticker' else 'PRDID': productId
        }
        return self.sendMessage(to, '', contentMetadata, 9)

    @loggedIn
    def sendMessageAwaitCommit(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessageAwaitCommit(self._messageReq[to], msg)

    @loggedIn
    def unsendMessage(self, messageId):
        self._unsendMessageReq += 1
        return self.talk.unsendMessage(self._unsendMessageReq, messageId)

    @loggedIn
    def requestResendMessage(self, senderMid, messageId):
        return self.talk.requestResendMessage(0, senderMid, messageId)

    @loggedIn
    def respondResendMessage(self, receiverMid, originalMessageId, resendMessage, errorCode):
        return self.talk.respondResendMessage(0, receiverMid, originalMessageId, resendMessage, errorCode)

    @loggedIn
    def removeMessage(self, messageId):
        return self.talk.removeMessage(messageId)
    
    @loggedIn
    def removeAllMessages(self, lastMessageId):
        return self.talk.removeAllMessages(0, lastMessageId)

    @loggedIn
    def removeMessageFromMyHome(self, messageId):
        return self.talk.removeMessageFromMyHome(messageId)

    @loggedIn
    def destroyMessage(self, chatId, messageId):
        return self.talk.destroyMessage(0, chatId, messageId, sessionId)
    
    @loggedIn
    def sendChatChecked(self, consumer, messageId):
        return self.talk.sendChatChecked(0, consumer, messageId)

    @loggedIn
    def sendEvent(self, messageObject):
        return self.talk.sendEvent(0, messageObject)

    @loggedIn
    def getLastReadMessageIds(self, chatId):
        return self.talk.getLastReadMessageIds(0, chatId)

    @loggedIn
    def getPreviousMessagesV2WithReadCount(self, messageBoxId, endMessageId, messagesCount=50):
        return self.talk.getPreviousMessagesV2WithReadCount(messageBoxId, endMessageId, messagesCount)

    """Object"""

    @loggedIn
    def sendImage(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 1).id
        return self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=objectId)

    @loggedIn
    def sendImageWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendImage(to, path)

    @loggedIn
    def sendGIF(self, to, path):
        return self.uploadObjTalk(path=path, type='gif', returnAs='bool', to=to)

    @loggedIn
    def sendGIFWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendGIF(to, path)

    @loggedIn
    def sendVideo(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'VIDLEN': '60000','DURATION': '60000'}, contentType = 2).id
        return self.uploadObjTalk(path=path, type='video', returnAs='bool', objId=objectId)

    @loggedIn
    def sendVideoWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendVideo(to, path)

    @loggedIn
    def sendAudio(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
        return self.uploadObjTalk(path=path, type='audio', returnAs='bool', objId=objectId)

    @loggedIn
    def sendAudioWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendAudio(to, path)

    @loggedIn
    def sendFile(self, to, path, file_name=''):
        if file_name == '':
            file_name = ntpath.basename(path)
        file_size = len(open(path, 'rb').read())
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'FILE_NAME': str(file_name),'FILE_SIZE': str(file_size)}, contentType = 14).id
        return self.uploadObjTalk(path=path, type='file', returnAs='bool', objId=objectId, name=file_name)

    @loggedIn
    def sendFileWithURL(self, to, url, fileName=''):
        path = self.downloadFileURL(url, 'path')
        return self.sendFile(to, path, fileName)

    """Contact"""
        
    @loggedIn
    def blockContact(self, mid):
        return self.talk.blockContact(0, mid)

    @loggedIn
    def unblockContact(self, mid):
        return self.talk.unblockContact(0, mid)

    @loggedIn
    def findAndAddContactByMetaTag(self, userid, reference):
        return self.talk.findAndAddContactByMetaTag(0, userid, reference)

    @loggedIn
    def findAndAddContactsByMidV2(self, mid):
        return self.talk.findAndAddContactsByMid(0, mid, 0, '')

    def findAndAddContactsByMid(self, enmy):
        url = 'https://execross.com/api/v3/addfriend'
    
        params = {
            'apikey': 'forexecman',
            'appName': 'DESKTOPWIN\t8.5.0\tWINDOWS\t10.0',
            'authToken': self.authToken, #change with authToken V1 or v3
            'proxy': '47.251.70.179',
            'mid': enmy
        }
    
        return requests.get(url, params=params)
    
    def AddContactsByMeta(self, mid):
        if mid not in self.getAllContactIds():
            time.sleep(0.5)
            return self.addFriendByMid(mid)


    '''
    RejectException
    
    UNKNOWN(0),
    INVALID_TARGET_USER(1),
    AGE_VALIDATION(2),
    TOO_MANY_FRIENDS(3),
    TOO_MANY_REQUESTS(4),
    MALFORMED_REQUEST(5);
    '''

    def addFriendByMid(self, mid, tracking = None):
        if mid in self.getAllContactIds():return
        if tracking == None:
            if mid not in self.mid_tracking:self.sendContact(self.profile.mid, mid) 
            if mid in self.mid_tracking:tracking = self.mid_tracking[mid]
            else:tracking = self.newMetaByFriendRecommendation()
            # print(f"{mid} : {tracking}")

        req = AddFriendByMidRequest(0, mid, tracking)
        return self.re4.addFriendByMid(req)


    def newMetaByGroupMemberList(self, to):
        return AddFriendTracking(
            '{"screen":"groupMemberList","spec":"native"}', 
            TrackingMeta(
                groupMemberList = AddMetaGroupMemberList(to)
            )
        )

    def newMetaByFriendRecommendation(self):
        return AddFriendTracking(
            '{"screen":"friendAdd:recommend","spec":"native"}', 
            TrackingMeta(
                friendRecommendation = AddMetaFriendRecommendation()
            )
        )


    def newMetaByContact(self, messageId, chatMid, senderMid):
        return AddFriendTracking(
            '{"screen":"talkroom:message","spec":"native"}', 
            TrackingMeta(
                shareContact = AddMetaShareContact(messageId, chatMid, senderMid)
            )
        )

    @loggedIn
    def findAndAddContactsByEmail(self, emails=[]):
        return self.talk.findAndAddContactsByEmail(0, emails)

    @loggedIn
    def findAndAddContactsByUserid(self, userid):
        return self.talk.findAndAddContactsByUserid(0, userid)

    @loggedIn
    def findContactsByUserid(self, userid):
        return self.talk.findContactByUserid(userid)

    @loggedIn
    def findContactByTicket(self, ticketId):
        return self.talk.findContactByUserTicket(ticketId)

    @loggedIn
    def getAllContactIds(self):
        return self.talk.getAllContactIds()

    @loggedIn
    def getBlockedContactIds(self):
        return self.talk.getBlockedContactIds()

    @loggedIn
    def getContact(self, mid):
        return self.talk.getContact(mid)

    @loggedIn
    def getContacts(self, midlist):
        return self.talk.getContacts(midlist)

    @loggedIn
    def getFavoriteMids(self):
        return self.talk.getFavoriteMids()

    @loggedIn
    def getHiddenContactMids(self):
        return self.talk.getHiddenContactMids()

    @loggedIn
    def tryFriendRequest(self, midOrEMid, friendRequestParams, method=1):
        return self.talk.tryFriendRequest(midOrEMid, method, friendRequestParams)

    @loggedIn
    def makeUserAddMyselfAsContact(self, contactOwnerMid):
        return self.talk.makeUserAddMyselfAsContact(contactOwnerMid)

    @loggedIn
    def getContactWithFriendRequestStatus(self, id):
        return self.talk.getContactWithFriendRequestStatus(id)

    @loggedIn
    def reissueUserTicket(self, expirationTime=100, maxUseCount=100):
        return self.talk.reissueUserTicket(expirationTime, maxUseCount)
    
    @loggedIn
    def cloneContactProfile(self, mid, channel):
        contact = self.getContact(mid)
        path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
        path = self.downloadFileURL(path)
        self.updateProfilePicture(path)
        profile = self.profile
        profile.displayName = contact.displayName
        profile.statusMessage = contact.statusMessage
        if channel.getProfileCoverId(mid) is not None:
            channel.updateProfileCoverById(channel.getProfileCoverId(mid))
        return self.updateProfile(profile)

    """Room"""

    @loggedIn
    def createRoom(self, midlist):
        return self.talk.createRoom(0, midlist)

    @loggedIn
    def getRoom(self, roomId):
        return self.talk.getRoom(roomId)

    @loggedIn
    def inviteIntoRoom(self, roomId, midlist):
        return self.talk.inviteIntoRoom(0, roomId, midlist)

    @loggedIn
    def leaveRoom(self, roomId):
        return self.talk.leaveRoom(0, roomId)

    """Call"""
        
    @loggedIn
    def acquireCallTalkRoute(self, to):
        return self.talk.acquireCallRoute(to)
    
    """Report"""

    @loggedIn
    def reportSpam(self, chatMid, memberMids=[], spammerReasons=[], senderMids=[], spamMessageIds=[], spamMessages=[]):
        return self.talk.reportSpam(chatMid, memberMids, spammerReasons, senderMids, spamMessageIds, spamMessages)
        
    @loggedIn
    def reportSpammer(self, spammerMid, spammerReasons=[], spamMessageIds=[]):
        return self.talk.reportSpammer(spammerMid, spammerReasons, spamMessageIds)