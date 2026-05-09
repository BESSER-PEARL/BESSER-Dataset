





import java.util.List;
import java.util.ArrayList;

public class publication_PublicationStructure extends Named {






    private List<publication_Paper> publication_papers;


    public publication_PublicationStructure(
    ) {
        super(
        );
        this.publication_papers = new ArrayList<>();
    }

    public publication_PublicationStructure(
        ArrayList<publication_Paper> publication_papers    ) {
        this.publication_papers = publication_papers;
    }


    public List<publication_Paper> getPublication_papers() {
        return publication_papers;
    }

    public void addPublication_paper(Publication_paper publication_paper) {
        this.publication_papers.add(publication_paper);
    }

}