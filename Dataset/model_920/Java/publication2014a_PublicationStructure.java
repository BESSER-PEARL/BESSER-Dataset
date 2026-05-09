





import java.util.List;
import java.util.ArrayList;

public class publication2014a_PublicationStructure extends Named {






    private List<publication2014a_Paper> publication2014a_papers;


    public publication2014a_PublicationStructure(
    ) {
        super(
        );
        this.publication2014a_papers = new ArrayList<>();
    }

    public publication2014a_PublicationStructure(
        ArrayList<publication2014a_Paper> publication2014a_papers    ) {
        this.publication2014a_papers = publication2014a_papers;
    }


    public List<publication2014a_Paper> getPublication2014a_papers() {
        return publication2014a_papers;
    }

    public void addPublication2014a_paper(Publication2014a_paper publication2014a_paper) {
        this.publication2014a_papers.add(publication2014a_paper);
    }

}