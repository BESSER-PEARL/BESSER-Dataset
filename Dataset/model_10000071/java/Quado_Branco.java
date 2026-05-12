





import java.util.List;
import java.util.ArrayList;

public class Quado_Branco  {

    private int cont_no;
    private String member_pwd;
    private String address;
    private String dob;
    private String fname;
    private String lname;
    private String gender;
    private int member_id;





    private List<Members> memberss;




    private List<Retro_Projetor> retro_projetors;


    public Quado_Branco(
        int cont_no,        String member_pwd,        String address,        String dob,        String fname,        String lname,        String gender,        int member_id    ) {
        this.cont_no = cont_no;
        this.member_pwd = member_pwd;
        this.address = address;
        this.dob = dob;
        this.fname = fname;
        this.lname = lname;
        this.gender = gender;
        this.member_id = member_id;
        this.memberss = new ArrayList<>();
        this.retro_projetors = new ArrayList<>();
    }

    public Quado_Branco(
        int cont_no,        String member_pwd,        String address,        String dob,        String fname,        String lname,        String gender,        int member_id        ArrayList<Members> memberss,        ArrayList<Retro_Projetor> retro_projetors    ) {
        this.cont_no = cont_no;
        this.member_pwd = member_pwd;
        this.address = address;
        this.dob = dob;
        this.fname = fname;
        this.lname = lname;
        this.gender = gender;
        this.member_id = member_id;
        this.memberss = memberss;
        this.retro_projetors = retro_projetors;
    }

    public int getCont_no() {
        return cont_no;
    }

    public void setCont_no(int cont_no) {
        this.cont_no = cont_no;
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
    public String getDob() {
        return dob;
    }

    public void setDob(String dob) {
        this.dob = dob;
    }
    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }
    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public int getMember_id() {
        return member_id;
    }

    public void setMember_id(int member_id) {
        this.member_id = member_id;
    }

    public List<Members> getMemberss() {
        return memberss;
    }

    public void addMembers(Members members) {
        this.memberss.add(members);
    }
    public List<Retro_Projetor> getRetro_projetors() {
        return retro_projetors;
    }

    public void addRetro_projetor(Retro_projetor retro_projetor) {
        this.retro_projetors.add(retro_projetor);
    }

}