





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String Certification;
    private String Languages;
    private String Education;





    private Department department;


    public Staff(
        String Certification,        String Languages,        String Education    ) {
        this.Certification = Certification;
        this.Languages = Languages;
        this.Education = Education;
    }


    public String getCertification() {
        return Certification;
    }

    public void setCertification(String Certification) {
        this.Certification = Certification;
    }
    public String getLanguages() {
        return Languages;
    }

    public void setLanguages(String Languages) {
        this.Languages = Languages;
    }
    public String getEducation() {
        return Education;
    }

    public void setEducation(String Education) {
        this.Education = Education;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

}