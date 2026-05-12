





import java.util.List;
import java.util.ArrayList;

public class Members  {

    private String dob;
    private int member_id;
    private String lname;
    private String member_pwd;
    private String address;
    private String gender;
    private String fname;
    private int cont_no;



    public Members(
        String dob,        int member_id,        String lname,        String member_pwd,        String address,        String gender,        String fname,        int cont_no    ) {
        this.dob = dob;
        this.member_id = member_id;
        this.lname = lname;
        this.member_pwd = member_pwd;
        this.address = address;
        this.gender = gender;
        this.fname = fname;
        this.cont_no = cont_no;
    }


    public String getDob() {
        return dob;
    }

    public void setDob(String dob) {
        this.dob = dob;
    }
    public int getMember_id() {
        return member_id;
    }

    public void setMember_id(int member_id) {
        this.member_id = member_id;
    }
    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }
    public String getMember_pwd() {
        return member_pwd;
    }

    public void setMember_pwd(String member_pwd) {
        this.member_pwd = member_pwd;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }
    public int getCont_no() {
        return cont_no;
    }

    public void setCont_no(int cont_no) {
        this.cont_no = cont_no;
    }


}