

from tsa_waiver. tsa_website import login_tsa_website, \
    create_new_waiver, \
    create_list_input, \
    read_tsa_waiver_text, save_draft

if __name__ == "__main__":

    session = login_tsa_website()
    #create_new_waiver(session)
    #read_tsa_waiver_text()
    save_draft(session)


