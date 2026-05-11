





import java.util.List;
import java.util.ArrayList;

public class studyprogram_Department  {

    private String name;





    private List<studyprogram_Program> studyprogram_programs;




    private List<studyprogram_Course> studyprogram_courses;


    public studyprogram_Department(
        String name    ) {
        this.name = name;
        this.studyprogram_programs = new ArrayList<>();
        this.studyprogram_courses = new ArrayList<>();
    }

    public studyprogram_Department(
        String name        ArrayList<studyprogram_Program> studyprogram_programs,        ArrayList<studyprogram_Course> studyprogram_courses    ) {
        this.name = name;
        this.studyprogram_programs = studyprogram_programs;
        this.studyprogram_courses = studyprogram_courses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<studyprogram_Program> getStudyprogram_programs() {
        return studyprogram_programs;
    }

    public void addStudyprogram_program(Studyprogram_program studyprogram_program) {
        this.studyprogram_programs.add(studyprogram_program);
    }
    public List<studyprogram_Course> getStudyprogram_courses() {
        return studyprogram_courses;
    }

    public void addStudyprogram_course(Studyprogram_course studyprogram_course) {
        this.studyprogram_courses.add(studyprogram_course);
    }

}