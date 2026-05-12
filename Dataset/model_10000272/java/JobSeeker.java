





import java.util.List;
import java.util.ArrayList;

public class JobSeeker  {

    private String Experience;
    private String Qualification;
    private String Name;





    private Administrator administrator;


    public JobSeeker(
        String Experience,        String Qualification,        String Name    ) {
        this.Experience = Experience;
        this.Qualification = Qualification;
        this.Name = Name;
    }


    public String getExperience() {
        return Experience;
    }

    public void setExperience(String Experience) {
        this.Experience = Experience;
    }
    public String getQualification() {
        return Qualification;
    }

    public void setQualification(String Qualification) {
        this.Qualification = Qualification;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }

}