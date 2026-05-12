





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private int phonenumber;
    private String sex;
    private String firstname;
    private int blood_group;
    private String email;
    private int birthyear;
    private String addr;
    private String lastname;
    private int id;





    private Doctor doctor;


    public Patient(
        int phonenumber,        String sex,        String firstname,        int blood_group,        String email,        int birthyear,        String addr,        String lastname,        int id    ) {
        this.phonenumber = phonenumber;
        this.sex = sex;
        this.firstname = firstname;
        this.blood_group = blood_group;
        this.email = email;
        this.birthyear = birthyear;
        this.addr = addr;
        this.lastname = lastname;
        this.id = id;
    }


    public int getPhonenumber() {
        return phonenumber;
    }

    public void setPhonenumber(int phonenumber) {
        this.phonenumber = phonenumber;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public int getBlood_group() {
        return blood_group;
    }

    public void setBlood_group(int blood_group) {
        this.blood_group = blood_group;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getBirthyear() {
        return birthyear;
    }

    public void setBirthyear(int birthyear) {
        this.birthyear = birthyear;
    }
    public String getAddr() {
        return addr;
    }

    public void setAddr(String addr) {
        this.addr = addr;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(Doctor doctor) {
        this.doctor = doctor;
    }

}