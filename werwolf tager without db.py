from apscheduler.schedulers.background import BackgroundScheduler
from pyrogram import Client, filters
import pyrogram
from pyrogram.types import Message, Chat 
from pyrogram.raw import functions, types
from time import *
import asyncio


#ADMIN = 148178781
app = Client(
    "my_account",
    api_id=api_id,
    api_hash=api_hash
)

creator_list = [148178781,1289379153,5242938533,1614558689]
A_list = [148178781,885455619]
m_list = []
msg_list = []
activated_chat = []
common_chats = []
all_chats = []
group_on = []
wwt = open("wwt").read()
a = (wwt.split(']['))
b = a[0]
c = b[1:]
a[0] = c
q = a[-1]
v = q[:-1]
a[-1] = v
for i in a :
    if int(i) not in activated_chat :

        activated_chat.append(int(i))




def update() :
    
    ch = app.get_common_chats('Relationshiper')
    for i in ch :
        if int(i.id) not in common_chats :
            common_chats.append(int(i.id))
    

    for dialog in app.iter_dialogs():
        if dialog.chat.type == "supergroup" :
            if int(dialog.chat.id) not in all_chats :
                all_chats.append((dialog.chat.id))
                
        elif dialog.chat.type == "group" :
            if int(dialog.chat.id) not in all_chats :
                all_chats.append(int(dialog.chat.id))
        else:
            continue
    




    wwt = open("wwt").read()
    a = (wwt.split(']['))
    b = a[0]
    c = b[1:]
    a[0] = c
    q = a[-1]
    v = q[:-1]
    a[-1] = v
    for i in a :
        
        if int(i) not in activated_chat :
            activated_chat.append(int(i))
            
        else :
            continue
        
    for i in activated_chat :
        if str([i]) not in wwt : 
            activated_chat.remove(i) 
        else :
            continue 
    
    for i in all_chats :
        if i not in activated_chat :
            if i not in common_chats : 
                print(i)
                app.send_message(i,'این گروه فعال نمیباشد ، جهت فعال سازی به آیدی @Relationshiper پیام دهید')
                sleep(5)
                app.leave_chat(i)
                all_chats.remove(i)
    
    #print(common_chats)
    #print(all_chats)
    #print(activated_chat)
    return activated_chat , all_chats , common_chats
    

#def func(_, __, query):
#    return query.data == "py"

#static_data_filter = filters.create(func('_', '__',))
@app.on_message(filters.command('cache') & filters.user(creator_list) & filters.chat(-1001205550644))      
def my_handler5(_:Client, m:Message):
    chat_id = m.chat.id
    m_id = m.message_id
    user_id = m.from_user.id
    ch = app.get_common_chats(1289379153)
    for i in ch :
        if int(i.id) not in common_chats :
            common_chats.append(int(i.id))
    
    for dialog in app.iter_dialogs():
        if dialog.chat.type == "supergroup" :
            if int(dialog.chat.id) not in all_chats :
                all_chats.append(int(dialog.chat.id))
        elif dialog.chat.type == "group" :
            if int(dialog.chat.id) not in all_chats :
                all_chats.append(int(dialog.chat.id))
    m.reply('cahced successfully')
    a = app.get_chat_member(chat_id,user_id)
    print(a.can_pin_messages)
    if a.can_pin_messages == True :
        print('yes')
    
@app.on_message(filters.user(175844556) & filters.media)
def tag(_:Client, m:Message):
    cpt = m.caption
    text = m.text
    x = int(0)
    wtext = m.entities
    command = m.command
    chat_id = m.chat.id
    m_id = m.message_id
    cmc = app.get_chat_members_count(chat_id)
    cmc = int(cmc)
    if cmc <= 50 :
        cmco = cmc 
    else :
        cmco = 203
    cmco = int(cmco)

    if cpt.startswith("یک بازی با حالت"):
        m_id = m.message_id
        info = app.get_messages(chat_id,m_id)
        if int(chat_id) in activated_chat :
            if int(chat_id) in group_on :  
                while "reply_markup" in str(app.get_messages(chat_id,m_id)):      
                    msg_list.append([chat_id,m_id,[]])
                    infff = info.reply_markup.inline_keyboard 
                    infe = infff[0]
                    infl = infe[0].url
                    txx = infe[0].text
            
                    if "reply_markup" not in str(app.get_messages(chat_id,m_id))  :
                        break
                
                    tmb = ""
                    cnt = int(0)
      
                    for member in app.iter_chat_members(chat_id, cmco, filter = "recent"):
                        ln = len(msg_list)
                        tmb += f"[{member.user.first_name}](tg://user?id={member.user.id})\n ^^^^^^^^^ \n"
                        cnt += 1
                        if cnt == 7  :
                            e = app.send_message(chat_id ,tmb + f"\n\n[ازینجا {txx}]({infl})",disable_web_page_preview=infl)
                            tmb = ""
                            cnt = 0
                            sleep(5)
                        else :
                            continue                        
                        for i in range(ln) :
                            n = msg_list[i]
                            if chat_id == n[0] :
                                if m_id == n[1] :
                                    n[2].append(e.message_id)
                                else:
                                    continue
                            else :
                                continue
             
                    x += 1
                    if x > 0 :
                        break         


    while msg_list :
        lnn = len(msg_list)
        for i in range(lnn) :
            j = msg_list[i]
            cid = int(j[0])
            sid = int(j[1])
            
            if "reply_markup" not in str(app.get_messages(cid,sid))  :
                app.delete_messages(cid,j[2])
                del(msg_list[i])
                lnn = len(msg_list)
                print(msg_list)
                sleep(5)
                break
                
            else :
                sleep(5)
                continue
             
           

            
            
            

        
        
    
    infoo = app.get_messages(chat_id,m_id)
    #print (info)
    if "reply_markup" in str(infoo) : 
        print("yyyyy")
    else : 
        print("nnnn")


@app.on_message(filters.command('activate') & filters.user(creator_list) )#& filters.chat(common_chats)
def my_handler(_:Client, m:Message):
    chat_id = m.chat.id 
    command = m.command
    text = m.text
    chat_id = m.chat.id
    user_id = m.from_user.id
    del command[0]
    a = command[0]
    if a == "wwt" : 
        act_file = open("wwt").read()
        if str([chat_id]) in act_file :
            inf_msg = m.reply('این گروه قبلا به گروه های فعال اضافه شده است')
            sleep(10)
            app.delete_messages(chat_id,inf_msg.message_id)
        else :
            try :
                open("wwt","a+").writelines(str([chat_id]))
                add_msg = m.reply('این گروه با موفقیت فعال شد')
                sleep(10)
                app.delete_messages(chat_id,add_msg.message_id)
            except :
                err_msg = m.reply('خطایی پیش آمد ، لطفا بعدا تلاش کنید')
                sleep(10)
                app.delete_messages(chat_id,err_msg.message_id)

    else :
        pass
        
@app.on_message(filters.command('deactivate') & filters.user(creator_list) & ~filters.chat(-1001205550644) )
def my_handler(_:Client, m:Message):
    a_chat = []
    cnt = int(0)
    chat_id = m.chat.id 
    command = m.command
    text = m.text
    chat_id = m.chat.id
    user_id = m.from_user.id
    del command[0]
    a = command[0]
    if a == "wwt" : 
        print("hi")
        wwt = open("wwt").read()
        a = (wwt.split(']['))
        b = a[0]
        c = b[1:]
        a[0] = c
        q = a[-1]
        v = q[:-1]
        a[-1] = v
        for i in a :
            i = int(i)
            a_chat.append(int(i))
        if chat_id in a_chat:
            try :
                a_chat.remove(chat_id)
                print(a_chat)
                del_msg = m.reply('این گروه با موفقیت غیرفعال شد')
                for i in a_chat :
                    if cnt == 0 :
                        open("wwt","w+").writelines(str([i]))
                        cnt += 1
                    else :
                        open("wwt","a+").writelines(str([i]))
                cnt = 0 
                sleep(5)
                app.delete_messages(chat_id,del_msg.message_id)
                app.leave_chat(chat_id)
                
            except :
                err_msg = m.reply('خطا،لطفا دوباره تلاش کنید')
                sleep(5)
                app.delete_messages(chat_id,err_msg.message_id)


        else :
            inf_msg = m.reply('این گروه ثبلا غیر فعال شده یا فعال نشده است')
            sleep(5)
            app.delete_messages(chat_id,inf_msg.message_id)
    else :
        pass

@app.on_message(filters.command('t') & filters.user(creator_list) )
def my_handler(_:Client, m:Message):
    print(activated_chat)
@app.on_message(filters.command('tageron')  & ~filters.private )
def my_handler(_:Client, m:Message):
    a_chat = []
    cnt = int(0)
    chat_id = m.chat.id 
    command = m.command
    text = m.text
    chat_id = m.chat.id
    user_id = m.from_user.id
    if command[1] == 'wwt' :
        del command[0]
        a = command[0]
    if a == "wwt" : 
        tgr_on = open('tageron').read()
        a = (tgr_on.split(']['))
        b = a[0]
        c = b[1:]
        a[0] = c
        q = a[-1]
        v = q[:-1]
        a[-1] = v
        for i in a :
            if int(i) not in group_on :
                group_on.append(int(i))

        
        if int(chat_id) in activated_chat :
            
            user_sts = app.get_chat_member(chat_id,user_id)
            user_status = user_sts.status
            my_sts = app.get_chat_member(chat_id,'me')
           
            if my_sts.status == 'administrator' :
                if  my_sts.can_invite_users == True & my_sts.can_delete_messages == True & my_sts.can_pin_messages == True :
                    
                    if user_status == 'creator'   :
                        if int(chat_id) not in group_on :
                            try :
                                open("tageron","a+").writelines( str([chat_id]))
                                group_on.append(int(chat_id))
                                on_mesg = m.reply('تگر با موفقیت در گروه شما فعال شد')
                                sleep(10)
                                app.delete_messages(chat_id,on_mesg.message_id)
                            except :
                                err_mesg = m.reply('خطایی پیش امد لطفا دوباره تلاش کنید')
                                sleep(10)
                                app.delete_messages(chat_id,err_mesg.message_id)
                        else : 
                            info_mesg = m.reply('تگر همین الانشم تو این گروه فعاله')
                            sleep(10)
                            app.delete_messages(chat_id,info_mesg.message_id)
                    elif user_status == 'administrator' :
                        if int(chat_id) not in group_on :
                            no_prms = m.reply('شما مالک گروه نیستید')
                            sleep(5)
                            app.delete_messages(chat_id,no_prms.message_id)
                
                        else : 
                            inf_mesg = m.reply('تگر همین الانشم تو این گروه فعاله')
                            sleep(10)
                            app.delete_messages(chat_id,inf_mesg.message_id)
                    elif user_status == 'member' :
                        no_prms = m.reply('شما فقط یک چصه ممبر هستید')
                        sleep(5)
                        app.delete_messages(chat_id,no_prms.message_id)

            
                else :
                    prms_err = m.reply('لطفا ربات را ادمین گروه کرده و سه دسترسی (حذف پیام،سنجاق کردن پیام ها و دعوت کاربران از طریق لینک(افرودن عضو)) را به ربات بدهید') 
                    sleep(15)
                    app.delete_messages(chat_id,prms_err.message_id)

            else : 
                adm_msg = m.reply('لطفا ابتدا ربات را در گروه خود ادمین کنید')
                sleep(10)
                app.delete_messages(chat_id,adm_msg)
                print('ok')




            

@app.on_message(filters.command('tageroff') & ~filters.private )
def my_handler(_:Client, m:Message):
    a_chat = []
    cntt = int(0)
    chat_id = m.chat.id 
    command = m.command
    text = m.text
    chat_id = m.chat.id
    user_id = m.from_user.id
    if command[1] == 'wwt' :
        del command[0]
        a = command[0]
    if a == "wwt" : 
        tgr_on = open('tageron').read()
        a = (tgr_on.split(']['))
        b = a[0]
        c = b[1:]
        a[0] = c
        q = a[-1]
        v = q[:-1]
        a[-1] = v
        for i in a :
            if int(i) in group_on :

                user_sts = app.get_chat_member(chat_id,user_id)
                user_status = user_sts.status
                if user_status == 'creator'   :
                    if int(chat_id) not in group_on :
                        try :
                            group_on.remove(i)
                            off_msg = m.reply('این گروه با موفقیت خاموش شد')
                            sleep(5)
                            app.delete_messages(chat_id,off_msg.message_id)
                            for i in group_on :
                                if cntt == 0 :

                                    open("wwt","w+").writelines(str([i]))
                                    cntt += 1
                                else :
                                    open("wwt","a+").writelines(str([i]))
                            cntt = 0 
                      
                        

                        except :
                            err_mesg = m.reply('خطایی پیش امد لطفا دوباره تلاش کنید')
                            sleep(10)
                            app.delete_messages(chat_id,err_mesg.message_id)
                    else : 
                        info_mesg = m.reply('تگر همین الانشم تو این گروه خاموشه')
                        sleep(10)
                        app.delete_messages(chat_id,info_mesg.message_id)
                elif user_status == 'administrator' :
                    if int(chat_id) not in group_on :
                        no_prms = m.reply('شما مالک گروه نیستید')
                        sleep(5)
                        app.delete_messages(chat_id,no_prms.message_id)
                
                    else : 
                        inf_mesg = m.reply('تگر همین الانشم تو این گروه فعاله')
                        sleep(10)
                        app.delete_messages(chat_id,inf_mesg.message_id)
                elif user_status == 'member' :
                    no_prms = m.reply('شما فقط یک چصه ممبر هستید')
                    sleep(5)
                    app.delete_messages(chat_id,no_prms.message_id)













                
            else : 
                noff_msg = m.reply('این گروه قبلا روشن نشده است ')
                sleep(5)
                app.delete_messages(chat_id,noff_msg.message_id)
                continue

        


scheduler = BackgroundScheduler()
scheduler.add_job(update, "interval", seconds=30)




scheduler.start()


app.run()