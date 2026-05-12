





import java.util.List;
import java.util.ArrayList;

public class project_University extends Organization {






    private List<project_Student> project_students;




    private project_Student project_student;




    private List<project_Enrollment> project_enrollments;




    private project_Enrollment project_enrollment;


    public project_University(
    ) {
        super(
        );
        this.project_students = new ArrayList<>();
        this.project_enrollments = new ArrayList<>();
    }

    public project_University(
        ArrayList<project_Student> project_students,        ArrayList<project_Enrollment> project_enrollments    ) {
        this.project_students = project_students;
        this.project_enrollments = project_enrollments;
    }


    public List<project_Student> getProject_students() {
        return project_students;
    }

    public void addProject_student(Project_student project_student) {
        this.project_students.add(project_student);
    }
    public project_Student getProject_student() {
        return project_student;
    }

    public void setProject_student(project_Student project_student) {
        this.project_student = project_student;
    }
    public List<project_Enrollment> getProject_enrollments() {
        return project_enrollments;
    }

    public void addProject_enrollment(Project_enrollment project_enrollment) {
        this.project_enrollments.add(project_enrollment);
    }
    public project_Enrollment getProject_enrollment() {
        return project_enrollment;
    }

    public void setProject_enrollment(project_Enrollment project_enrollment) {
        this.project_enrollment = project_enrollment;
    }

}