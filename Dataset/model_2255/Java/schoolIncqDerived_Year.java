





import java.util.List;
import java.util.ArrayList;

public class schoolIncqDerived_Year  {

    private int startingDate;





    private schoolIncqDerived_School schoolincqderived_school;




    private schoolIncqDerived_School schoolincqderived_school;




    private schoolIncqDerived_School schoolincqderived_school;




    private schoolIncqDerived_SchoolClass schoolincqderived_schoolclass;




    private List<schoolIncqDerived_SchoolClass> schoolincqderived_schoolclasss;


    public schoolIncqDerived_Year(
        int startingDate    ) {
        this.startingDate = startingDate;
        this.schoolincqderived_schoolclasss = new ArrayList<>();
    }

    public schoolIncqDerived_Year(
        int startingDate        ArrayList<schoolIncqDerived_SchoolClass> schoolincqderived_schoolclasss    ) {
        this.startingDate = startingDate;
        this.schoolincqderived_schoolclasss = schoolincqderived_schoolclasss;
    }

    public int getStartingdate() {
        return startingDate;
    }

    public void setStartingdate(int startingDate) {
        this.startingDate = startingDate;
    }

    public schoolIncqDerived_School getSchoolincqderived_school() {
        return schoolincqderived_school;
    }

    public void setSchoolincqderived_school(schoolIncqDerived_School schoolincqderived_school) {
        this.schoolincqderived_school = schoolincqderived_school;
    }
    public schoolIncqDerived_School getSchoolincqderived_school() {
        return schoolincqderived_school;
    }

    public void setSchoolincqderived_school(schoolIncqDerived_School schoolincqderived_school) {
        this.schoolincqderived_school = schoolincqderived_school;
    }
    public schoolIncqDerived_School getSchoolincqderived_school() {
        return schoolincqderived_school;
    }

    public void setSchoolincqderived_school(schoolIncqDerived_School schoolincqderived_school) {
        this.schoolincqderived_school = schoolincqderived_school;
    }
    public schoolIncqDerived_SchoolClass getSchoolincqderived_schoolclass() {
        return schoolincqderived_schoolclass;
    }

    public void setSchoolincqderived_schoolclass(schoolIncqDerived_SchoolClass schoolincqderived_schoolclass) {
        this.schoolincqderived_schoolclass = schoolincqderived_schoolclass;
    }
    public List<schoolIncqDerived_SchoolClass> getSchoolincqderived_schoolclasss() {
        return schoolincqderived_schoolclasss;
    }

    public void addSchoolincqderived_schoolclass(Schoolincqderived_schoolclass schoolincqderived_schoolclass) {
        this.schoolincqderived_schoolclasss.add(schoolincqderived_schoolclass);
    }

}