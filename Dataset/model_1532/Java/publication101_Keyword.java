





import java.util.List;
import java.util.ArrayList;

public class publication101_Keyword extends Named {

    private String description;





    private List<publication101_Paper> publication101_papers;




    private publication101_KnowledgeManager publication101_knowledgemanager;


    public publication101_Keyword(
        String description    ) {
        super(
        );
        this.description = description;
        this.publication101_papers = new ArrayList<>();
    }

    public publication101_Keyword(
        String description        ArrayList<publication101_Paper> publication101_papers    ) {
        this.description = description;
        this.publication101_papers = publication101_papers;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<publication101_Paper> getPublication101_papers() {
        return publication101_papers;
    }

    public void addPublication101_paper(Publication101_paper publication101_paper) {
        this.publication101_papers.add(publication101_paper);
    }
    public publication101_KnowledgeManager getPublication101_knowledgemanager() {
        return publication101_knowledgemanager;
    }

    public void setPublication101_knowledgemanager(publication101_KnowledgeManager publication101_knowledgemanager) {
        this.publication101_knowledgemanager = publication101_knowledgemanager;
    }

}