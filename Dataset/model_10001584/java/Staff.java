





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String gender;
    private String position;
    private int contact;
    private int Staff_ID;
    private String address;
    private String lname;
    private String fname;
    private String password;
    private String email;
    private String username;



    public Staff(
        String gender,        String position,        int contact,        int Staff_ID,        String address,        String lname,        String fname,        String password,        String email,        String username    ) {
        this.gender = gender;
        this.position = position;
        this.contact = contact;
        this.Staff_ID = Staff_ID;
        this.address = address;
        this.lname = lname;
        this.fname = fname;
        this.password = password;
        this.email = email;
        this.username = username;
    }


    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public int getContact() {
        return contact;
    }

    public void setContact(int contact) {
        this.contact = contact;
    }
    public int getStaff_id() {
        return Staff_ID;
    }

    public void setStaff_id(int Staff_ID) {
        this.Staff_ID = Staff_ID;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
    }
    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}