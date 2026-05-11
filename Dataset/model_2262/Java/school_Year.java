





import java.util.List;
import java.util.ArrayList;

public class school_Year  {

    private int startingDate;





    private school_School school_school;




    private List<school_SchoolClass> school_schoolclasss;




    private school_SchoolClass school_schoolclass;




    private school_School school_school;


    public school_Year(
        int startingDate    ) {
        this.startingDate = startingDate;
        this.school_schoolclasss = new ArrayList<>();
    }

    public school_Year(
        int startingDate        ArrayList<school_SchoolClass> school_schoolclasss    ) {
        this.startingDate = startingDate;
        this.school_schoolclasss = school_schoolclasss;
    }

    public int getStartingdate() {
        return startingDate;
    }

    public void setStartingdate(int startingDate) {
        this.startingDate = startingDate;
    }

    public school_School getSchool_school() {
        return school_school;
    }

    public void setSchool_school(school_School school_school) {
        this.school_school = school_school;
    }
    public List<school_SchoolClass> getSchool_schoolclasss() {
        return school_schoolclasss;
    }

    public void addSchool_schoolclass(School_schoolclass school_schoolclass) {
        this.school_schoolclasss.add(school_schoolclass);
    }
    public school_SchoolClass getSchool_schoolclass() {
        return school_schoolclass;
    }

    public void setSchool_schoolclass(school_SchoolClass school_schoolclass) {
        this.school_schoolclass = school_schoolclass;
    }
    public school_School getSchool_school() {
        return school_school;
    }

    public void setSchool_school(school_School school_school) {
        this.school_school = school_school;
    }

}