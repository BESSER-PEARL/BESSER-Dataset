





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String lname;
    private String position;
    private String username;
    private String fname;
    private String gender;
    private String email;
    private String password;
    private String address;
    private int contact;
    private int Staff_ID;



    public Staff(
        String lname,        String position,        String username,        String fname,        String gender,        String email,        String password,        String address,        int contact,        int Staff_ID    ) {
        this.lname = lname;
        this.position = position;
        this.username = username;
        this.fname = fname;
        this.gender = gender;
        this.email = email;
        this.password = password;
        this.address = address;
        this.contact = contact;
        this.Staff_ID = Staff_ID;
    }


    public String getLname() {
        return lname;
    }

    public void setLname(String lname) {
        this.lname = lname;
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
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
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


}