from pyrogram.errors import FloodWait,Forbidden,BadRequest
from pyrogram import Client, filters
from pyrogram.types import Message, Chat
import os
import time
import random



app = Client(
    "my_account",
    api_id=api_id,
    api_hash=api_hash
)



grp_mmbr_list = []
final_notadd_list = []
target_gap = []
add_closed_list = []
attack_gap = []
all_chats = []




    
if os.path.exists("notadded_before") :
    add = open("notadded_before").read()
    a = (add.split(']['))
    b = a[0]
    c = b[1:]
    a[0] = c
    q = a[-1]
    v = q[:-1]
    a[-1] = v
    for i in a :
        add_closed_list.append(int(i))
else : 
    
    open("notadded_before","a+").write("[148178781][1616819766]")
    add = open("notadded_before").read()
    a = (add.split(']['))
    b = a[0]
    c = b[1:]
    a[0] = c
    q = a[-1]
    v = q[:-1]
    a[-1] = v
    for i in a :
        add_closed_list.append(int(i))
@app.on_message(filters.text & filters.user("me")) 
def my(_:Client , m:Message):
    chat_id = m.chat.id 
    text = m.text

    


    ### give the target to add member chat id as format -100x for sp group and x for group

    if text.startswith("to =") : 
        tar_wait = m.reply('ok,this proces will take 20-200 second,please wait')
        time.sleep(15)
        app.delete_messages(chat_id,tar_wait.message_id)
        target_gap.clear()
        q = text[5:]
        for dialog in app.iter_dialogs():
            if int(dialog.chat.id) not in all_chats :
                all_chats.append(int(dialog.chat.id))

        try :
            q = int(q)

            if int(q) in all_chats :   
                cht = app.get_chat(q)
                cht_typ = cht.type

                if cht_typ == "supergroup":
                    target_gap.append(q)
                    sg_set = m.reply(f"target set : {q}")
                    time.sleep(10)
                    app.delete_messages(chat_id,sg_set.message_id)
                
                elif cht_typ == "group":
                    target_gap.append(q)
                    g_set = m.reply(f"target group  set : {q}")
                    time.sleep(10)
                    app.delete_messages(chat_id,g_set.message_id)

                elif cht_typ == "private" :
                    p = m.reply("here is private chat,the target wasnt set")
                    time.sleep(10)
                    app.delete_messages(chat_id,p.message_id)

                elif cht_typ == 'channel' :
                    ch = m.reply("this is channel,the target wasnt set")
                    time.sleep(10)
                    app.delete_messages(chat_id,ch.message_id)
                else :
                    un = m.reply('unknown type,please try with another ids')
                    time.sleep(10)
                    app.delete_messages(chat_id,un.message_id)


            else : 
                na = m.reply("you are not joining in the chat or enter False format")
                time.sleep(10)
                app.delete_messages(chat_id,na.message_id)

        except ValueError :
            v_e = m.reply(f"ValueError,the    {q}    is not integer ")
            time.sleep(10)
            app.delete_messages(chat_id,v_e.message_id)

       ### give group to move members from there 
    if text.startswith("from =") : 
        att_wait = m.reply('ok,this proces will take 20-200 second,please wait')
        time.sleep(15)
        app.delete_messages(chat_id,att_wait.message_id)
        attack_gap.clear()
        from_id = text[7:]
        for dialog in app.iter_dialogs():
            if int(dialog.chat.id) not in all_chats :
                all_chats.append(int(dialog.chat.id))
        try :
            from_id = int(from_id)

            if int(from_id) in all_chats :   
                cht = app.get_chat(from_id)
                cht_typ = cht.type

                if cht_typ == "supergroup":
                    attack_gap.append(from_id)
                    sg_set = m.reply(f"attack set : {from_id}")
                    time.sleep(10)
                    app.delete_messages(chat_id,sg_set.message_id)
                
                elif cht_typ == "group":
                    attack_gap.append(from_id)
                    g_set = m.reply(f"attack group  set : {from_id}")
                    time.sleep(10)
                    app.delete_messages(chat_id,g_set.message_id)

                elif cht_typ == "private" :
                    p = m.reply("here is private chat,the target wasnt set")
                    time.sleep(10)
                    app.delete_messages(chat_id,p.message_id)

                elif cht_typ == 'channel' :
                    ch = m.reply("this is channel,the target wasnt set")
                    time.sleep(10)
                    app.delete_messages(chat_id,ch.message_id)
                else :
                    un = m.reply('unknown type,please try with another ids')
                    time.sleep(10)
                    app.delete_messages(chat_id,un.message_id)


            else : 
                na = m.reply("you are not joining in the chat or enter False format")
                time.sleep(10)
                app.delete_messages(chat_id,na.message_id)

        except ValueError :
            v_e = m.reply(f"ValueError,the    {from_id}    is not integer ")
            time.sleep(10)
            app.delete_messages(chat_id,v_e.message_id)

        ### do move

    if text == "start" :
        add_cnt = int(0)
        not_add = int(0)
        tried_bfr = int(0)
        total_time = 0
        rs = 'end'
        
        if len(target_gap) + len(attack_gap) == 2 :
            for member in app.iter_chat_members(target_gap[0]) :
                grp_mmbr_list.append(int(member.user.id))
                time.sleep(0.01)
            final_notadd_list = add_closed_list + grp_mmbr_list
            a = app.get_chat(target_gap[0])
            if a.permissions.can_invite_users == True : 
                tar_cnt = app.get_chat_members_count(int(target_gap[0]))
                tar_nm = app.get_chat(int(target_gap[0]))
                tar_name = tar_nm.title
                att_cnt = app.get_chat_members_count(int(attack_gap[0]))
                att_nm = app.get_chat(int(attack_gap[0]))
                att_name = att_nm.title

                app.send_message('me',f"   [STARTED]   \nfrom : {attack_gap}\nname : {att_name}\nwith {att_cnt} members \n\n to : {target_gap}\nname : {tar_name}\nwith {tar_cnt} members")
                for i in app.iter_chat_members(attack_gap[0]) :
                    t2 = random.randint(6,16)
                    t3 = random.randint(6,16)
                    t4 = random.randint(6,16)
                    t5 = random.randint(6,16)
                    t6 = random.randint(6,16)

                    if int(i.user.id) in final_notadd_list : 
                        print("tried before")
                        time.sleep(0.01)
                        tried_bfr += 1
                        total_time += (0.01)
                        continue
                    
                    
                    else :
                        try :
                            app.add_chat_members (target_gap[0] ,i.user.id)
                            time.sleep(t2)
                            print("added")
                            add_cnt += int(1)
                            total_time += t2
                        except FloodWait : 
                            rs == 'flood'
                            print("flood")
                            break
                        except Forbidden  : 
                            print("dont added")
                            not_add += int(1)
                            n = open("notadded_before").read()
                            if str([i.user.id]) in n :
                                time.sleep(t3)
                                total_time += t3
                                continue
                            else :
                                open("notadded_before","a+").writelines( str([i.user.id]))
                                time.sleep(t4)
                                total_time += t4
                                continue
                        except BadRequest : 
                            not_add += int(1)
                            print("dont added,badRequest")
                            n = open("notadded_before").read()
                            if str([i.user.id]) in n :
                                time.sleep(t5)
                                total_time += t5
                                continue
                            else :
                                open("notadded_before","a+").writelines( str([i.user.id]))
                                time.sleep(t6)
                                total_time += t6
                                continue
                        

                app.send_message('me',f'for group {attack_gap[0]} , tried {add_cnt+not_add+tried_bfr} time that {add_cnt} time done and {not_add} dont and {tried_bfr} is tried before to add,total time = {total_time} second,stop reason = {rs}')
           
            else :
                prms = m.reply('add member is closed in target gap')
                app.delete_messages(chat_id,prms.message_id)

        else :
            fill = m.reply('please fill two requeirment group')
            time.sleep(5)
            app.delete_messages(chat_id,fill.message_id)
    m.continue_propagation()

     ### get online status   
@app.on_message(filters.command("status") & filters.user("me"))
def my_handler3(_:Client , m:Message):
    chat_id = m.chat.id 
    sts = m.reply(f'the target gap = {target_gap} And attack gap = {attack_gap}')
    time.sleep(10)
    app.delete_messages(chat_id,sts.message_id)

@app.on_message(filters.command("help") & filters.user('me'))
def help(_:Client , m:Message):
    chat_id = m.chat.id 
    hp = m.reply('first you must give 2 group to bot,attack and target group , for atk gp => from = chatid that for simple groups = x and for super groups = -100x,and for target gp => to = chatid thr same way,and finally send => start ')
    time.sleep(30)
    app.delete_messages(chat_id,hp.message_id)



        

   



app.run()