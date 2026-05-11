





import java.util.List;
import java.util.ArrayList;

public class Projects_Training extends Project {






    private List<Projects_Qualification> projects_qualifications;




    private Projects_Qualification projects_qualification;


    public Projects_Training(
    ) {
        super(
        );
        this.projects_qualifications = new ArrayList<>();
    }

    public Projects_Training(
        ArrayList<Projects_Qualification> projects_qualifications    ) {
        this.projects_qualifications = projects_qualifications;
    }


    public List<Projects_Qualification> getProjects_qualifications() {
        return projects_qualifications;
    }

    public void addProjects_qualification(Projects_qualification projects_qualification) {
        this.projects_qualifications.add(projects_qualification);
    }
    public Projects_Qualification getProjects_qualification() {
        return projects_qualification;
    }

    public void setProjects_qualification(Projects_Qualification projects_qualification) {
        this.projects_qualification = projects_qualification;
    }

}