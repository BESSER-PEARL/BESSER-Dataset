





import java.util.List;
import java.util.ArrayList;

public class Classes_Guests_Guest  {

    private String stays;
    private String title;
    private String lastname;
    private String ssid;
    private String phone;
    private String firstname;
    private String email;
    private String requests;
    private String account;



    public Classes_Guests_Guest(
        String stays,        String title,        String lastname,        String ssid,        String phone,        String firstname,        String email,        String requests,        String account    ) {
        this.stays = stays;
        this.title = title;
        this.lastname = lastname;
        this.ssid = ssid;
        this.phone = phone;
        this.firstname = firstname;
        this.email = email;
        this.requests = requests;
        this.account = account;
    }


    public String getStays() {
        return stays;
    }

    public void setStays(String stays) {
        this.stays = stays;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getSsid() {
        return ssid;
    }

    public void setSsid(String ssid) {
        this.ssid = ssid;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getRequests() {
        return requests;
    }

    public void setRequests(String requests) {
        this.requests = requests;
    }
    public String getAccount() {
        return account;
    }

    public void setAccount(String account) {
        this.account = account;
    }


}