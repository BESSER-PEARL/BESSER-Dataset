





import java.util.List;
import java.util.ArrayList;

public class studyprogram_ObligatoryCourses  {






    private studyprogram_Program studyprogram_program;




    private List<studyprogram_Course> studyprogram_courses;




    private studyprogram_Program studyprogram_program;


    public studyprogram_ObligatoryCourses(
    ) {
        this.studyprogram_courses = new ArrayList<>();
    }

    public studyprogram_ObligatoryCourses(
        ArrayList<studyprogram_Course> studyprogram_courses    ) {
        this.studyprogram_courses = studyprogram_courses;
    }


    public studyprogram_Program getStudyprogram_program() {
        return studyprogram_program;
    }

    public void setStudyprogram_program(studyprogram_Program studyprogram_program) {
        this.studyprogram_program = studyprogram_program;
    }
    public List<studyprogram_Course> getStudyprogram_courses() {
        return studyprogram_courses;
    }

    public void addStudyprogram_course(Studyprogram_course studyprogram_course) {
        this.studyprogram_courses.add(studyprogram_course);
    }
    public studyprogram_Program getStudyprogram_program() {
        return studyprogram_program;
    }

    public void setStudyprogram_program(studyprogram_Program studyprogram_program) {
        this.studyprogram_program = studyprogram_program;
    }

}