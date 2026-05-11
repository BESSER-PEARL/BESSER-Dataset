





import java.util.List;
import java.util.ArrayList;

public class study_ElectiveCourseList  {






    private study_Semester study_semester;




    private List<study_Course> study_courses;




    private study_Semester study_semester;


    public study_ElectiveCourseList(
    ) {
        this.study_courses = new ArrayList<>();
    }

    public study_ElectiveCourseList(
        ArrayList<study_Course> study_courses    ) {
        this.study_courses = study_courses;
    }


    public study_Semester getStudy_semester() {
        return study_semester;
    }

    public void setStudy_semester(study_Semester study_semester) {
        this.study_semester = study_semester;
    }
    public List<study_Course> getStudy_courses() {
        return study_courses;
    }

    public void addStudy_course(Study_course study_course) {
        this.study_courses.add(study_course);
    }
    public study_Semester getStudy_semester() {
        return study_semester;
    }

    public void setStudy_semester(study_Semester study_semester) {
        this.study_semester = study_semester;
    }

}