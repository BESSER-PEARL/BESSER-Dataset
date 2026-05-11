





import java.util.List;
import java.util.ArrayList;

public class studyprogram_Department  {

    private String name;





    private studyprogram_Course studyprogram_course;




    private studyprogram_Program studyprogram_program;




    private List<studyprogram_Program> studyprogram_programs;




    private List<studyprogram_Course> studyprogram_courses;




    private studyprogram_University studyprogram_university;




    private studyprogram_University studyprogram_university;


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

    public studyprogram_Course getStudyprogram_course() {
        return studyprogram_course;
    }

    public void setStudyprogram_course(studyprogram_Course studyprogram_course) {
        this.studyprogram_course = studyprogram_course;
    }
    public studyprogram_Program getStudyprogram_program() {
        return studyprogram_program;
    }

    public void setStudyprogram_program(studyprogram_Program studyprogram_program) {
        this.studyprogram_program = studyprogram_program;
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
    public studyprogram_University getStudyprogram_university() {
        return studyprogram_university;
    }

    public void setStudyprogram_university(studyprogram_University studyprogram_university) {
        this.studyprogram_university = studyprogram_university;
    }
    public studyprogram_University getStudyprogram_university() {
        return studyprogram_university;
    }

    public void setStudyprogram_university(studyprogram_University studyprogram_university) {
        this.studyprogram_university = studyprogram_university;
    }

}