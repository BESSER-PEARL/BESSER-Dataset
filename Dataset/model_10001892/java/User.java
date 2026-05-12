





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String fName;
    private int phoneNumber;
    private String lName;
    private String cin;
    private String email;
    private int birthDate;



    public User(
        String fName,        int phoneNumber,        String lName,        String cin,        String email,        int birthDate    ) {
        this.fName = fName;
        this.phoneNumber = phoneNumber;
        this.lName = lName;
        this.cin = cin;
        this.email = email;
        this.birthDate = birthDate;
    }


    public String getFname() {
        return fName;
    }

    public void setFname(String fName) {
        this.fName = fName;
    }
    public int getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(int phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getLname() {
        return lName;
    }

    public void setLname(String lName) {
        this.lName = lName;
    }
    public String getCin() {
        return cin;
    }

    public void setCin(String cin) {
        this.cin = cin;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(int birthDate) {
        this.birthDate = birthDate;
    }


}