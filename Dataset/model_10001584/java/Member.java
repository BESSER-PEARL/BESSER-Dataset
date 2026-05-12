





import java.util.List;
import java.util.ArrayList;

public class Member  {

    private String dob;
    private String member_pwd;
    private String gender;
    private String lname;
    private int member_id;
    private int cont_no;
    private String fname;
    private String address;



    public Member(
        String dob,        String member_pwd,        String gender,        String lname,        int member_id,        int cont_no,        String fname,        String address    ) {
        this.dob = dob;
        this.member_pwd = member_pwd;
        this.gender = gender;
        this.lname = lname;
        this.member_id = member_id;
        this.cont_no = cont_no;
        this.fname = fname;
        this.address = address;
    }


    public String getDob() {
        return dob;
    }

    public void setDob(String dob) {
        this.dob = dob;
    }
    public String getMember_pwd() {
        return member_pwd;
    }

    public void setMember_pwd(String member_pwd) {
        this.member_pwd = member_pwd;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }
    public int getMember_id() {
        return member_id;
    }

    public void setMember_id(int member_id) {
        this.member_id = member_id;
    }
    public int getCont_no() {
        return cont_no;
    }

    public void setCont_no(int cont_no) {
        this.cont_no = cont_no;
    }
    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}