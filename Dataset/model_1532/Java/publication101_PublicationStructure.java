





import java.util.List;
import java.util.ArrayList;

public class publication101_PublicationStructure extends Named {






    private List<publication101_Paper> publication101_papers;




    private publication101_PublicationSystem publication101_publicationsystem;




    private publication101_KnowledgeManager publication101_knowledgemanager;


    public publication101_PublicationStructure(
    ) {
        super(
        );
        this.publication101_papers = new ArrayList<>();
    }

    public publication101_PublicationStructure(
        ArrayList<publication101_Paper> publication101_papers    ) {
        this.publication101_papers = publication101_papers;
    }


    public List<publication101_Paper> getPublication101_papers() {
        return publication101_papers;
    }

    public void addPublication101_paper(Publication101_paper publication101_paper) {
        this.publication101_papers.add(publication101_paper);
    }
    public publication101_PublicationSystem getPublication101_publicationsystem() {
        return publication101_publicationsystem;
    }

    public void setPublication101_publicationsystem(publication101_PublicationSystem publication101_publicationsystem) {
        this.publication101_publicationsystem = publication101_publicationsystem;
    }
    public publication101_KnowledgeManager getPublication101_knowledgemanager() {
        return publication101_knowledgemanager;
    }

    public void setPublication101_knowledgemanager(publication101_KnowledgeManager publication101_knowledgemanager) {
        this.publication101_knowledgemanager = publication101_knowledgemanager;
    }

}