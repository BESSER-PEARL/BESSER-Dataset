





import java.util.List;
import java.util.ArrayList;

public class SWRC_ResearchTopic extends Topic {






    private Project project;




    private List<AcademicStaff> academicstaffs;


    public SWRC_ResearchTopic(
    ) {
        super(
        );
        this.academicstaffs = new ArrayList<>();
    }

    public SWRC_ResearchTopic(
        ArrayList<AcademicStaff> academicstaffs    ) {
        this.academicstaffs = academicstaffs;
    }


    public Project getProject() {
        return project;
    }

    public void setProject(Project project) {
        this.project = project;
    }
    public List<AcademicStaff> getAcademicstaffs() {
        return academicstaffs;
    }

    public void addAcademicstaff(Academicstaff academicstaff) {
        this.academicstaffs.add(academicstaff);
    }

}