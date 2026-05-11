





import java.util.List;
import java.util.ArrayList;

public class studies_CourseInstance  {

    private int year;
    private String instanceName;
    private String semester;





    private studies_Semester studies_semester;




    private studies_StudyCourse studies_studycourse;




    private studies_Course studies_course;




    private studies_Course studies_course;


    public studies_CourseInstance(
        int year,        String instanceName,        String semester    ) {
        this.year = year;
        this.instanceName = instanceName;
        this.semester = semester;
    }


    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }
    public String getInstancename() {
        return instanceName;
    }

    public void setInstancename(String instanceName) {
        this.instanceName = instanceName;
    }
    public String getSemester() {
        return semester;
    }

    public void setSemester(String semester) {
        this.semester = semester;
    }

    public studies_Semester getStudies_semester() {
        return studies_semester;
    }

    public void setStudies_semester(studies_Semester studies_semester) {
        this.studies_semester = studies_semester;
    }
    public studies_StudyCourse getStudies_studycourse() {
        return studies_studycourse;
    }

    public void setStudies_studycourse(studies_StudyCourse studies_studycourse) {
        this.studies_studycourse = studies_studycourse;
    }
    public studies_Course getStudies_course() {
        return studies_course;
    }

    public void setStudies_course(studies_Course studies_course) {
        this.studies_course = studies_course;
    }
    public studies_Course getStudies_course() {
        return studies_course;
    }

    public void setStudies_course(studies_Course studies_course) {
        this.studies_course = studies_course;
    }

}