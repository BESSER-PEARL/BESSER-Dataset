





import java.util.List;
import java.util.ArrayList;

public class Classes_Staff_Staff  {

    private String phone;
    private String ssid;
    private String email;
    private String firstName;
    private String lastName;
    private String job;



    public Classes_Staff_Staff(
        String phone,        String ssid,        String email,        String firstName,        String lastName,        String job    ) {
        this.phone = phone;
        this.ssid = ssid;
        this.email = email;
        this.firstName = firstName;
        this.lastName = lastName;
        this.job = job;
    }


    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getSsid() {
        return ssid;
    }

    public void setSsid(String ssid) {
        this.ssid = ssid;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
    }


}