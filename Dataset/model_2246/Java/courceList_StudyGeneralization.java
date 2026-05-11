





import java.util.List;
import java.util.ArrayList;

public class courceList_StudyGeneralization  {

    private String name;
    private String campus;
    private String educationLevel;
    private int nrOfYears;
    private String abbreviation;





    private courceList_Department courcelist_department;




    private courceList_Department courcelist_department;


    public courceList_StudyGeneralization(
        String name,        String campus,        String educationLevel,        int nrOfYears,        String abbreviation    ) {
        this.name = name;
        this.campus = campus;
        this.educationLevel = educationLevel;
        this.nrOfYears = nrOfYears;
        this.abbreviation = abbreviation;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCampus() {
        return campus;
    }

    public void setCampus(String campus) {
        this.campus = campus;
    }
    public String getEducationlevel() {
        return educationLevel;
    }

    public void setEducationlevel(String educationLevel) {
        this.educationLevel = educationLevel;
    }
    public int getNrofyears() {
        return nrOfYears;
    }

    public void setNrofyears(int nrOfYears) {
        this.nrOfYears = nrOfYears;
    }
    public String getAbbreviation() {
        return abbreviation;
    }

    public void setAbbreviation(String abbreviation) {
        this.abbreviation = abbreviation;
    }

    public courceList_Department getCourcelist_department() {
        return courcelist_department;
    }

    public void setCourcelist_department(courceList_Department courcelist_department) {
        this.courcelist_department = courcelist_department;
    }
    public courceList_Department getCourcelist_department() {
        return courcelist_department;
    }

    public void setCourcelist_department(courceList_Department courcelist_department) {
        this.courcelist_department = courcelist_department;
    }

}