





import java.util.List;
import java.util.ArrayList;

public class SWRC_AcademicStaff extends Person {






    private List<Publication> publications;




    private Publication publication;


    public SWRC_AcademicStaff(
    ) {
        super(
        );
        this.publications = new ArrayList<>();
    }

    public SWRC_AcademicStaff(
        ArrayList<Publication> publications    ) {
        this.publications = publications;
    }


    public List<Publication> getPublications() {
        return publications;
    }

    public void addPublication(Publication publication) {
        this.publications.add(publication);
    }
    public Publication getPublication() {
        return publication;
    }

    public void setPublication(Publication publication) {
        this.publication = publication;
    }

}