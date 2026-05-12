





import java.util.List;
import java.util.ArrayList;

public class network_TransactionManager  {

    private None con;





    private dao_AccountBanDAO2 dao_accountbandao2;




    private network_InsertCommentMess network_insertcommentmess;




    private dao_ProfileDAO dao_profiledao;




    private dao_ProfessionDAO dao_professiondao;




    private dao_ImagesDAO dao_imagesdao;




    private dao_FriendsDAO dao_friendsdao;




    private network_InsertComment network_insertcomment;




    private dao_LikesDAO dao_likesdao;




    private network_LoginProcess network_loginprocess;




    private dao_AccountBanDAO dao_accountbandao;




    private dao_MessageDAO dao_messagedao;




    private dao_CommentDAO dao_commentdao;




    private dao_TableDAO dao_tabledao;




    private dao_AdultDetectionDAO dao_adultdetectiondao;




    private dao_FriendRequestsDAO dao_friendrequestsdao;




    private dao_WarningDAO dao_warningdao;




    private network_InsertMessage network_insertmessage;




    private dao_UserDAO dao_userdao;


    public network_TransactionManager(
        None con    ) {
        this.con = con;
    }


    public None getCon() {
        return con;
    }

    public void setCon(None con) {
        this.con = con;
    }

    public dao_AccountBanDAO2 getDao_accountbandao2() {
        return dao_accountbandao2;
    }

    public void setDao_accountbandao2(dao_AccountBanDAO2 dao_accountbandao2) {
        this.dao_accountbandao2 = dao_accountbandao2;
    }
    public network_InsertCommentMess getNetwork_insertcommentmess() {
        return network_insertcommentmess;
    }

    public void setNetwork_insertcommentmess(network_InsertCommentMess network_insertcommentmess) {
        this.network_insertcommentmess = network_insertcommentmess;
    }
    public dao_ProfileDAO getDao_profiledao() {
        return dao_profiledao;
    }

    public void setDao_profiledao(dao_ProfileDAO dao_profiledao) {
        this.dao_profiledao = dao_profiledao;
    }
    public dao_ProfessionDAO getDao_professiondao() {
        return dao_professiondao;
    }

    public void setDao_professiondao(dao_ProfessionDAO dao_professiondao) {
        this.dao_professiondao = dao_professiondao;
    }
    public dao_ImagesDAO getDao_imagesdao() {
        return dao_imagesdao;
    }

    public void setDao_imagesdao(dao_ImagesDAO dao_imagesdao) {
        this.dao_imagesdao = dao_imagesdao;
    }
    public dao_FriendsDAO getDao_friendsdao() {
        return dao_friendsdao;
    }

    public void setDao_friendsdao(dao_FriendsDAO dao_friendsdao) {
        this.dao_friendsdao = dao_friendsdao;
    }
    public network_InsertComment getNetwork_insertcomment() {
        return network_insertcomment;
    }

    public void setNetwork_insertcomment(network_InsertComment network_insertcomment) {
        this.network_insertcomment = network_insertcomment;
    }
    public dao_LikesDAO getDao_likesdao() {
        return dao_likesdao;
    }

    public void setDao_likesdao(dao_LikesDAO dao_likesdao) {
        this.dao_likesdao = dao_likesdao;
    }
    public network_LoginProcess getNetwork_loginprocess() {
        return network_loginprocess;
    }

    public void setNetwork_loginprocess(network_LoginProcess network_loginprocess) {
        this.network_loginprocess = network_loginprocess;
    }
    public dao_AccountBanDAO getDao_accountbandao() {
        return dao_accountbandao;
    }

    public void setDao_accountbandao(dao_AccountBanDAO dao_accountbandao) {
        this.dao_accountbandao = dao_accountbandao;
    }
    public dao_MessageDAO getDao_messagedao() {
        return dao_messagedao;
    }

    public void setDao_messagedao(dao_MessageDAO dao_messagedao) {
        this.dao_messagedao = dao_messagedao;
    }
    public dao_CommentDAO getDao_commentdao() {
        return dao_commentdao;
    }

    public void setDao_commentdao(dao_CommentDAO dao_commentdao) {
        this.dao_commentdao = dao_commentdao;
    }
    public dao_TableDAO getDao_tabledao() {
        return dao_tabledao;
    }

    public void setDao_tabledao(dao_TableDAO dao_tabledao) {
        this.dao_tabledao = dao_tabledao;
    }
    public dao_AdultDetectionDAO getDao_adultdetectiondao() {
        return dao_adultdetectiondao;
    }

    public void setDao_adultdetectiondao(dao_AdultDetectionDAO dao_adultdetectiondao) {
        this.dao_adultdetectiondao = dao_adultdetectiondao;
    }
    public dao_FriendRequestsDAO getDao_friendrequestsdao() {
        return dao_friendrequestsdao;
    }

    public void setDao_friendrequestsdao(dao_FriendRequestsDAO dao_friendrequestsdao) {
        this.dao_friendrequestsdao = dao_friendrequestsdao;
    }
    public dao_WarningDAO getDao_warningdao() {
        return dao_warningdao;
    }

    public void setDao_warningdao(dao_WarningDAO dao_warningdao) {
        this.dao_warningdao = dao_warningdao;
    }
    public network_InsertMessage getNetwork_insertmessage() {
        return network_insertmessage;
    }

    public void setNetwork_insertmessage(network_InsertMessage network_insertmessage) {
        this.network_insertmessage = network_insertmessage;
    }
    public dao_UserDAO getDao_userdao() {
        return dao_userdao;
    }

    public void setDao_userdao(dao_UserDAO dao_userdao) {
        this.dao_userdao = dao_userdao;
    }

}