





import java.util.List;
import java.util.ArrayList;

public class Librarian  {

    private int member_id;
    private String dob;
    private String member_pwd;
    private String address;
    private String fname;
    private int cont_no;
    private String gender;
    private String lname;





    private List<Member> members;




    private List<Books> bookss;


    public Librarian(
        int member_id,        String dob,        String member_pwd,        String address,        String fname,        int cont_no,        String gender,        String lname    ) {
        this.member_id = member_id;
        this.dob = dob;
        this.member_pwd = member_pwd;
        this.address = address;
        this.fname = fname;
        this.cont_no = cont_no;
        this.gender = gender;
        this.lname = lname;
        this.members = new ArrayList<>();
        this.bookss = new ArrayList<>();
    }

    public Librarian(
        int member_id,        String dob,        String member_pwd,        String address,        String fname,        int cont_no,        String gender,        String lname        ArrayList<Member> members,        ArrayList<Books> bookss    ) {
        this.member_id = member_id;
        this.dob = dob;
        this.member_pwd = member_pwd;
        this.address = address;
        this.fname = fname;
        this.cont_no = cont_no;
        this.gender = gender;
        this.lname = lname;
        this.members = members;
        this.bookss = bookss;
    }

    public int getMember_id() {
        return member_id;
    }

    public void setMember_id(int member_id) {
        this.member_id = member_id;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
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

    public List<Member> getMembers() {
        return members;
    }

    public void addMember(Member member) {
        this.members.add(member);
    }
    public List<Books> getBookss() {
        return bookss;
    }

    public void addBooks(Books books) {
        this.bookss.add(books);
    }

}