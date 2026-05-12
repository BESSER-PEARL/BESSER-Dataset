





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String joined;
    private String languages;
    private String certification;
    private String education;



    public Staff(
        String joined,        String languages,        String certification,        String education    ) {
        this.joined = joined;
        this.languages = languages;
        this.certification = certification;
        this.education = education;
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


}