





import java.util.List;
import java.util.ArrayList;

public class grudi_PersonInfo  {

    private String id;
    private String name;
    private String userName;
    private String phoneNumber;
    private String gender;





    private grudi_TeamLine grudi_teamline;


    public grudi_PersonInfo(
        String id,        String name,        String userName,        String phoneNumber,        String gender    ) {
        this.id = id;
        this.name = name;
        this.userName = userName;
        this.phoneNumber = phoneNumber;
        this.gender = gender;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public grudi_TeamLine getGrudi_teamline() {
        return grudi_teamline;
    }

    public void setGrudi_teamline(grudi_TeamLine grudi_teamline) {
        this.grudi_teamline = grudi_teamline;
    }

}