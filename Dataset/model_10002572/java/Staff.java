





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String certification;
    private String education;
    private String UserName;
    private String Password;
    private String joined;
    private String languages;



    public Staff(
        String certification,        String education,        String UserName,        String Password,        String joined,        String languages    ) {
        this.certification = certification;
        this.education = education;
        this.UserName = UserName;
        this.Password = Password;
        this.joined = joined;
        this.languages = languages;
    }


    public String getCertification() {
        return certification;
    }

    public void setCertification(String certification) {
        this.certification = certification;
    }
    public String getEducation() {
        return education;
    }

    public void setEducation(String education) {
        this.education = education;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getJoined() {
        return joined;
    }

    public void setJoined(String joined) {
        this.joined = joined;
    }
    public String getLanguages() {
        return languages;
    }

    public void setLanguages(String languages) {
        this.languages = languages;
    }


}