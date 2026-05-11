





import java.util.List;
import java.util.ArrayList;

public class study_Specialisation  {

    private String requirement;
    private String name;





    private study_Department study_department;




    private study_Semester study_semester;




    private List<study_Semester> study_semesters;




    private study_Department study_department;




    private study_Student study_student;




    private study_Program study_program;




    private study_Student study_student;




    private study_Program study_program;


    public study_Specialisation(
        String requirement,        String name    ) {
        this.requirement = requirement;
        this.name = name;
        this.study_semesters = new ArrayList<>();
    }

    public study_Specialisation(
        String requirement,        String name        ArrayList<study_Semester> study_semesters    ) {
        this.requirement = requirement;
        this.name = name;
        this.study_semesters = study_semesters;
    }

    public String getRequirement() {
        return requirement;
    }

    public void setRequirement(String requirement) {
        this.requirement = requirement;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public study_Department getStudy_department() {
        return study_department;
    }

    public void setStudy_department(study_Department study_department) {
        this.study_department = study_department;
    }
    public study_Semester getStudy_semester() {
        return study_semester;
    }

    public void setStudy_semester(study_Semester study_semester) {
        this.study_semester = study_semester;
    }
    public List<study_Semester> getStudy_semesters() {
        return study_semesters;
    }

    public void addStudy_semester(Study_semester study_semester) {
        this.study_semesters.add(study_semester);
    }
    public study_Department getStudy_department() {
        return study_department;
    }

    public void setStudy_department(study_Department study_department) {
        this.study_department = study_department;
    }
    public study_Student getStudy_student() {
        return study_student;
    }

    public void setStudy_student(study_Student study_student) {
        this.study_student = study_student;
    }
    public study_Program getStudy_program() {
        return study_program;
    }

    public void setStudy_program(study_Program study_program) {
        this.study_program = study_program;
    }
    public study_Student getStudy_student() {
        return study_student;
    }

    public void setStudy_student(study_Student study_student) {
        this.study_student = study_student;
    }
    public study_Program getStudy_program() {
        return study_program;
    }

    public void setStudy_program(study_Program study_program) {
        this.study_program = study_program;
    }

}