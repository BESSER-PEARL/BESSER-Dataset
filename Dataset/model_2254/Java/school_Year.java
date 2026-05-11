





import java.util.List;
import java.util.ArrayList;

public class school_Year  {

    private int weightOfRegularCourses;
    private int startingDate;





    private List<school_SchoolClass> school_schoolclasss;




    private school_School school_school;




    private school_School school_school;




    private school_SchoolClass school_schoolclass;




    private school_School school_school;


    public school_Year(
        int weightOfRegularCourses,        int startingDate    ) {
        this.weightOfRegularCourses = weightOfRegularCourses;
        this.startingDate = startingDate;
        this.school_schoolclasss = new ArrayList<>();
    }

    public school_Year(
        int weightOfRegularCourses,        int startingDate        ArrayList<school_SchoolClass> school_schoolclasss    ) {
        this.weightOfRegularCourses = weightOfRegularCourses;
        this.startingDate = startingDate;
        this.school_schoolclasss = school_schoolclasss;
    }

    public int getWeightofregularcourses() {
        return weightOfRegularCourses;
    }

    public void setWeightofregularcourses(int weightOfRegularCourses) {
        this.weightOfRegularCourses = weightOfRegularCourses;
    }
    public int getStartingdate() {
        return startingDate;
    }

    public void setStartingdate(int startingDate) {
        this.startingDate = startingDate;
    }

    public List<school_SchoolClass> getSchool_schoolclasss() {
        return school_schoolclasss;
    }

    public void addSchool_schoolclass(School_schoolclass school_schoolclass) {
        this.school_schoolclasss.add(school_schoolclass);
    }
    public school_School getSchool_school() {
        return school_school;
    }

    public void setSchool_school(school_School school_school) {
        this.school_school = school_school;
    }
    public school_School getSchool_school() {
        return school_school;
    }

    public void setSchool_school(school_School school_school) {
        this.school_school = school_school;
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