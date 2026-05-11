




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class lobj_User  {

    private String entryasxml;
    private LocalDate onlinedate;
    private String dossierasxml;
    private String photo;
    private String scn;
    private String authenticateldap;
    private String notificationprofileasxml;
    private String onlinestatus;
    private String firstname;
    private LocalDate currlogindate;
    private String password;
    private String lastname;
    private String id;
    private String fromext;
    private LocalDate inchatsince;
    private String lastcoursematerialviewnr;
    private String icqnumber;
    private String loginname;
    private String photochanged;
    private String chatroomnr;
    private String matriculationnr;
    private String datafilter;
    private String languagenr;
    private String lastcoursematerialnr;
    private String icqpassword;
    private LocalDate contchatdate;
    private LocalDate lastlogindate;





    private lobj_AccessControl lobj_accesscontrol;




    private lobj_AccessControl lobj_accesscontrol;




    private lobj_CourseMeta lobj_coursemeta;




    private lobj_AccessControl lobj_accesscontrol;


    public lobj_User(
        String entryasxml,        LocalDate onlinedate,        String dossierasxml,        String photo,        String scn,        String authenticateldap,        String notificationprofileasxml,        String onlinestatus,        String firstname,        LocalDate currlogindate,        String password,        String lastname,        String id,        String fromext,        LocalDate inchatsince,        String lastcoursematerialviewnr,        String icqnumber,        String loginname,        String photochanged,        String chatroomnr,        String matriculationnr,        String datafilter,        String languagenr,        String lastcoursematerialnr,        String icqpassword,        LocalDate contchatdate,        LocalDate lastlogindate    ) {
        this.entryasxml = entryasxml;
        this.onlinedate = onlinedate;
        this.dossierasxml = dossierasxml;
        this.photo = photo;
        this.scn = scn;
        this.authenticateldap = authenticateldap;
        this.notificationprofileasxml = notificationprofileasxml;
        this.onlinestatus = onlinestatus;
        this.firstname = firstname;
        this.currlogindate = currlogindate;
        this.password = password;
        this.lastname = lastname;
        this.id = id;
        this.fromext = fromext;
        this.inchatsince = inchatsince;
        this.lastcoursematerialviewnr = lastcoursematerialviewnr;
        this.icqnumber = icqnumber;
        this.loginname = loginname;
        this.photochanged = photochanged;
        this.chatroomnr = chatroomnr;
        this.matriculationnr = matriculationnr;
        this.datafilter = datafilter;
        this.languagenr = languagenr;
        this.lastcoursematerialnr = lastcoursematerialnr;
        this.icqpassword = icqpassword;
        this.contchatdate = contchatdate;
        this.lastlogindate = lastlogindate;
    }


    public String getEntryasxml() {
        return entryasxml;
    }

    public void setEntryasxml(String entryasxml) {
        this.entryasxml = entryasxml;
    }
    public LocalDate getOnlinedate() {
        return onlinedate;
    }

    public void setOnlinedate(LocalDate onlinedate) {
        this.onlinedate = onlinedate;
    }
    public String getDossierasxml() {
        return dossierasxml;
    }

    public void setDossierasxml(String dossierasxml) {
        this.dossierasxml = dossierasxml;
    }
    public String getPhoto() {
        return photo;
    }

    public void setPhoto(String photo) {
        this.photo = photo;
    }
    public String getScn() {
        return scn;
    }

    public void setScn(String scn) {
        this.scn = scn;
    }
    public String getAuthenticateldap() {
        return authenticateldap;
    }

    public void setAuthenticateldap(String authenticateldap) {
        this.authenticateldap = authenticateldap;
    }
    public String getNotificationprofileasxml() {
        return notificationprofileasxml;
    }

    public void setNotificationprofileasxml(String notificationprofileasxml) {
        this.notificationprofileasxml = notificationprofileasxml;
    }
    public String getOnlinestatus() {
        return onlinestatus;
    }

    public void setOnlinestatus(String onlinestatus) {
        this.onlinestatus = onlinestatus;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public LocalDate getCurrlogindate() {
        return currlogindate;
    }

    public void setCurrlogindate(LocalDate currlogindate) {
        this.currlogindate = currlogindate;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getFromext() {
        return fromext;
    }

    public void setFromext(String fromext) {
        this.fromext = fromext;
    }
    public LocalDate getInchatsince() {
        return inchatsince;
    }

    public void setInchatsince(LocalDate inchatsince) {
        this.inchatsince = inchatsince;
    }
    public String getLastcoursematerialviewnr() {
        return lastcoursematerialviewnr;
    }

    public void setLastcoursematerialviewnr(String lastcoursematerialviewnr) {
        this.lastcoursematerialviewnr = lastcoursematerialviewnr;
    }
    public String getIcqnumber() {
        return icqnumber;
    }

    public void setIcqnumber(String icqnumber) {
        this.icqnumber = icqnumber;
    }
    public String getLoginname() {
        return loginname;
    }

    public void setLoginname(String loginname) {
        this.loginname = loginname;
    }
    public String getPhotochanged() {
        return photochanged;
    }

    public void setPhotochanged(String photochanged) {
        this.photochanged = photochanged;
    }
    public String getChatroomnr() {
        return chatroomnr;
    }

    public void setChatroomnr(String chatroomnr) {
        this.chatroomnr = chatroomnr;
    }
    public String getMatriculationnr() {
        return matriculationnr;
    }

    public void setMatriculationnr(String matriculationnr) {
        this.matriculationnr = matriculationnr;
    }
    public String getDatafilter() {
        return datafilter;
    }

    public void setDatafilter(String datafilter) {
        this.datafilter = datafilter;
    }
    public String getLanguagenr() {
        return languagenr;
    }

    public void setLanguagenr(String languagenr) {
        this.languagenr = languagenr;
    }
    public String getLastcoursematerialnr() {
        return lastcoursematerialnr;
    }

    public void setLastcoursematerialnr(String lastcoursematerialnr) {
        this.lastcoursematerialnr = lastcoursematerialnr;
    }
    public String getIcqpassword() {
        return icqpassword;
    }

    public void setIcqpassword(String icqpassword) {
        this.icqpassword = icqpassword;
    }
    public LocalDate getContchatdate() {
        return contchatdate;
    }

    public void setContchatdate(LocalDate contchatdate) {
        this.contchatdate = contchatdate;
    }
    public LocalDate getLastlogindate() {
        return lastlogindate;
    }

    public void setLastlogindate(LocalDate lastlogindate) {
        this.lastlogindate = lastlogindate;
    }

    public lobj_AccessControl getLobj_accesscontrol() {
        return lobj_accesscontrol;
    }

    public void setLobj_accesscontrol(lobj_AccessControl lobj_accesscontrol) {
        this.lobj_accesscontrol = lobj_accesscontrol;
    }
    public lobj_AccessControl getLobj_accesscontrol() {
        return lobj_accesscontrol;
    }

    public void setLobj_accesscontrol(lobj_AccessControl lobj_accesscontrol) {
        this.lobj_accesscontrol = lobj_accesscontrol;
    }
    public lobj_CourseMeta getLobj_coursemeta() {
        return lobj_coursemeta;
    }

    public void setLobj_coursemeta(lobj_CourseMeta lobj_coursemeta) {
        this.lobj_coursemeta = lobj_coursemeta;
    }
    public lobj_AccessControl getLobj_accesscontrol() {
        return lobj_accesscontrol;
    }

    public void setLobj_accesscontrol(lobj_AccessControl lobj_accesscontrol) {
        this.lobj_accesscontrol = lobj_accesscontrol;
    }

}