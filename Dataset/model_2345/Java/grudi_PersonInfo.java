





import java.util.List;
import java.util.ArrayList;

public class grudi_PersonInfo  {

    private String name;
    private String phoneNumber;
    private String id;
    private String gender;
    private String userName;



    public grudi_PersonInfo(
        String name,        String phoneNumber,        String id,        String gender,        String userName    ) {
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.id = id;
        this.gender = gender;
        this.userName = userName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }


}