





import java.util.List;
import java.util.ArrayList;

public class Librarian  {

    private int cont_no;
    private String dob;
    private String fname;
    private String address;
    private int member_id;
    private String member_pwd;
    private String lname;
    private String gender;





    private List<Member> members;




    private List<Books> bookss;


    public Librarian(
        int cont_no,        String dob,        String fname,        String address,        int member_id,        String member_pwd,        String lname,        String gender    ) {
        this.cont_no = cont_no;
        this.dob = dob;
        this.fname = fname;
        this.address = address;
        this.member_id = member_id;
        this.member_pwd = member_pwd;
        this.lname = lname;
        this.gender = gender;
        this.members = new ArrayList<>();
        this.bookss = new ArrayList<>();
    }

    public Librarian(
        int cont_no,        String dob,        String fname,        String address,        int member_id,        String member_pwd,        String lname,        String gender        ArrayList<Member> members,        ArrayList<Books> bookss    ) {
        this.cont_no = cont_no;
        this.dob = dob;
        this.fname = fname;
        this.address = address;
        this.member_id = member_id;
        this.member_pwd = member_pwd;
        this.lname = lname;
        this.gender = gender;
        this.members = members;
        this.bookss = bookss;
    }

    public int getCont_no() {
        return cont_no;
    }

    public void setCont_no(int cont_no) {
        this.cont_no = cont_no;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getMember_id() {
        return member_id;
    }

    public void setMember_id(int member_id) {
        this.member_id = member_id;
    }
    public String getMember_pwd() {
        return member_pwd;
    }

    public void setMember_pwd(String member_pwd) {
        this.member_pwd = member_pwd;
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