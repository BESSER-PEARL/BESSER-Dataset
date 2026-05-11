





import java.util.List;
import java.util.ArrayList;

public class study_University  {

    private String name;





    private study_StudyProgramme study_studyprogramme;




    private List<study_Course> study_courses;




    private study_Student study_student;




    private study_Course study_course;




    private List<study_StudyProgramme> study_studyprogrammes;




    private List<study_Student> study_students;


    public study_University(
        String name    ) {
        this.name = name;
        this.study_courses = new ArrayList<>();
        this.study_studyprogrammes = new ArrayList<>();
        this.study_students = new ArrayList<>();
    }

    public study_University(
        String name        ArrayList<study_Course> study_courses,        ArrayList<study_StudyProgramme> study_studyprogrammes,        ArrayList<study_Student> study_students    ) {
        this.name = name;
        this.study_courses = study_courses;
        this.study_studyprogrammes = study_studyprogrammes;
        this.study_students = study_students;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public study_StudyProgramme getStudy_studyprogramme() {
        return study_studyprogramme;
    }

    public void setStudy_studyprogramme(study_StudyProgramme study_studyprogramme) {
        this.study_studyprogramme = study_studyprogramme;
    }
    public List<study_Course> getStudy_courses() {
        return study_courses;
    }

    public void addStudy_course(Study_course study_course) {
        this.study_courses.add(study_course);
    }
    public study_Student getStudy_student() {
        return study_student;
    }

    public void setStudy_student(study_Student study_student) {
        this.study_student = study_student;
    }
    public study_Course getStudy_course() {
        return study_course;
    }

    public void setStudy_course(study_Course study_course) {
        this.study_course = study_course;
    }
    public List<study_StudyProgramme> getStudy_studyprogrammes() {
        return study_studyprogrammes;
    }

    public void addStudy_studyprogramme(Study_studyprogramme study_studyprogramme) {
        this.study_studyprogrammes.add(study_studyprogramme);
    }
    public List<study_Student> getStudy_students() {
        return study_students;
    }

    public void addStudy_student(Study_student study_student) {
        this.study_students.add(study_student);
    }

}