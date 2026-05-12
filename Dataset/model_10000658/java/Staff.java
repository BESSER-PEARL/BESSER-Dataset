





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private int Staff_ID;
    private String position;
    private String username;
    private String fname;
    private String email;
    private String lname;
    private String password;
    private String address;
    private String gender;
    private int contact;



    public Staff(
        int Staff_ID,        String position,        String username,        String fname,        String email,        String lname,        String password,        String address,        String gender,        int contact    ) {
        this.Staff_ID = Staff_ID;
        this.position = position;
        this.username = username;
        this.fname = fname;
        this.email = email;
        this.lname = lname;
        this.password = password;
        this.address = address;
        this.gender = gender;
        this.contact = contact;
    }


    public int getStaff_id() {
        return Staff_ID;
    }

    public void setStaff_id(int Staff_ID) {
        this.Staff_ID = Staff_ID;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
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
    public int getContact() {
        return contact;
    }

    public void setContact(int contact) {
        this.contact = contact;
    }


}