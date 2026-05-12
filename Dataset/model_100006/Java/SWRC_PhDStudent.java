





import java.util.List;
import java.util.ArrayList;

public class SWRC_PhDStudent extends Graduate {






    private Project project;




    private List<Publication> publications;




    private AcademicStaff academicstaff;


    public SWRC_PhDStudent(
    ) {
        super(
        );
        this.publications = new ArrayList<>();
    }

    public SWRC_PhDStudent(
        ArrayList<Publication> publications    ) {
        this.publications = publications;
    }


    public Project getProject() {
        return project;
    }

    public void setProject(Project project) {
        this.project = project;
    }
    public List<Publication> getPublications() {
        return publications;
    }

    public void addPublication(Publication publication) {
        this.publications.add(publication);
    }
    public AcademicStaff getAcademicstaff() {
        return academicstaff;
    }

    public void setAcademicstaff(AcademicStaff academicstaff) {
        this.academicstaff = academicstaff;
    }

}