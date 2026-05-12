





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String Certification;
    private String Status;
    private String Education;
    private String Joined;
    private String Languages;



    public Staff(
        String Certification,        String Status,        String Education,        String Joined,        String Languages    ) {
        this.Certification = Certification;
        this.Status = Status;
        this.Education = Education;
        this.Joined = Joined;
        this.Languages = Languages;
    }


    public String getCertification() {
        return Certification;
    }

    public void setCertification(String Certification) {
        this.Certification = Certification;
    }
    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public String getEducation() {
        return Education;
    }

    public void setEducation(String Education) {
        this.Education = Education;
    }
    public String getJoined() {
        return Joined;
    }

    public void setJoined(String Joined) {
        this.Joined = Joined;
    }
    public String getLanguages() {
        return Languages;
    }

    public void setLanguages(String Languages) {
        this.Languages = Languages;
    }


}