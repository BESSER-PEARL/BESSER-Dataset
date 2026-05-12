





import java.util.List;
import java.util.ArrayList;

public class publication2014_PublicationStructure extends Named {






    private List<publication2014_Paper> publication2014_papers;




    private List<publication2014_Researcher> publication2014_researchers;


    public publication2014_PublicationStructure(
    ) {
        super(
        );
        this.publication2014_papers = new ArrayList<>();
        this.publication2014_researchers = new ArrayList<>();
    }

    public publication2014_PublicationStructure(
        ArrayList<publication2014_Paper> publication2014_papers,        ArrayList<publication2014_Researcher> publication2014_researchers    ) {
        this.publication2014_papers = publication2014_papers;
        this.publication2014_researchers = publication2014_researchers;
    }


    public List<publication2014_Paper> getPublication2014_papers() {
        return publication2014_papers;
    }

    public void addPublication2014_paper(Publication2014_paper publication2014_paper) {
        this.publication2014_papers.add(publication2014_paper);
    }
    public List<publication2014_Researcher> getPublication2014_researchers() {
        return publication2014_researchers;
    }

    public void addPublication2014_researcher(Publication2014_researcher publication2014_researcher) {
        this.publication2014_researchers.add(publication2014_researcher);
    }

}