





import java.util.List;
import java.util.ArrayList;

public class study_CourseSlot  {

    private boolean elective;





    private List<study_Course> study_courses;




    private study_Course study_course;




    private study_Semester study_semester;


    public study_CourseSlot(
        boolean elective    ) {
        this.elective = elective;
        this.study_courses = new ArrayList<>();
    }

    public study_CourseSlot(
        boolean elective        ArrayList<study_Course> study_courses    ) {
        this.elective = elective;
        this.study_courses = study_courses;
    }

    public boolean getElective() {
        return elective;
    }

    public void setElective(boolean elective) {
        this.elective = elective;
    }

    public List<study_Course> getStudy_courses() {
        return study_courses;
    }

    public void addStudy_course(Study_course study_course) {
        this.study_courses.add(study_course);
    }
    public study_Course getStudy_course() {
        return study_course;
    }

    public void setStudy_course(study_Course study_course) {
        this.study_course = study_course;
    }
    public study_Semester getStudy_semester() {
        return study_semester;
    }

    public void setStudy_semester(study_Semester study_semester) {
        this.study_semester = study_semester;
    }

}