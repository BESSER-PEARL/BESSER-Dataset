





import java.util.List;
import java.util.ArrayList;

public class project_Student extends Person {






    private project_Enrollment project_enrollment;




    private List<project_Enrollment> project_enrollments;


    public project_Student(
    ) {
        super(
        );
        this.project_enrollments = new ArrayList<>();
    }

    public project_Student(
        ArrayList<project_Enrollment> project_enrollments    ) {
        this.project_enrollments = project_enrollments;
    }


    public project_Enrollment getProject_enrollment() {
        return project_enrollment;
    }

    public void setProject_enrollment(project_Enrollment project_enrollment) {
        this.project_enrollment = project_enrollment;
    }
    public List<project_Enrollment> getProject_enrollments() {
        return project_enrollments;
    }

    public void addProject_enrollment(Project_enrollment project_enrollment) {
        this.project_enrollments.add(project_enrollment);
    }

}