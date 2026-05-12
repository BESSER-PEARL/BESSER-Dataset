





import java.util.List;
import java.util.ArrayList;

public class publication2014b_Paper extends Named {






    private publication2014b_Researcher publication2014b_researcher;




    private publication2014b_PublicationStructure publication2014b_publicationstructure;




    private List<publication2014b_Researcher> publication2014b_researchers;


    public publication2014b_Paper(
    ) {
        super(
        );
        this.publication2014b_researchers = new ArrayList<>();
    }

    public publication2014b_Paper(
        ArrayList<publication2014b_Researcher> publication2014b_researchers    ) {
        this.publication2014b_researchers = publication2014b_researchers;
    }


    public publication2014b_Researcher getPublication2014b_researcher() {
        return publication2014b_researcher;
    }

    public void setPublication2014b_researcher(publication2014b_Researcher publication2014b_researcher) {
        this.publication2014b_researcher = publication2014b_researcher;
    }
    public publication2014b_PublicationStructure getPublication2014b_publicationstructure() {
        return publication2014b_publicationstructure;
    }

    public void setPublication2014b_publicationstructure(publication2014b_PublicationStructure publication2014b_publicationstructure) {
        this.publication2014b_publicationstructure = publication2014b_publicationstructure;
    }
    public List<publication2014b_Researcher> getPublication2014b_researchers() {
        return publication2014b_researchers;
    }

    public void addPublication2014b_researcher(Publication2014b_researcher publication2014b_researcher) {
        this.publication2014b_researchers.add(publication2014b_researcher);
    }

}