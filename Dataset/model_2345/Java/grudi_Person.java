





import java.util.List;
import java.util.ArrayList;

public class grudi_Person  {

    private String phoneNumber;
    private String id;
    private String versionNumber;
    private String username;
    private String address;
    private String password;
    private String gender;
    private String name;
    private String email;



    public grudi_Person(
        String phoneNumber,        String id,        String versionNumber,        String username,        String address,        String password,        String gender,        String name,        String email    ) {
        this.phoneNumber = phoneNumber;
        this.id = id;
        this.versionNumber = versionNumber;
        this.username = username;
        this.address = address;
        this.password = password;
        this.gender = gender;
        this.name = name;
        this.email = email;
    }


    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getVersionnumber() {
        return versionNumber;
    }

    public void setVersionnumber(String versionNumber) {
        this.versionNumber = versionNumber;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}