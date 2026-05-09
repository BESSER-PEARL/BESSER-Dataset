





import java.util.List;
import java.util.ArrayList;

public class publication102_Keyword extends Named {

    private String description;





    private List<publication102_Paper> publication102_papers;




    private publication102_KnowledgeManager publication102_knowledgemanager;


    public publication102_Keyword(
        String description    ) {
        super(
        );
        this.description = description;
        this.publication102_papers = new ArrayList<>();
    }

    public publication102_Keyword(
        String description        ArrayList<publication102_Paper> publication102_papers    ) {
        this.description = description;
        this.publication102_papers = publication102_papers;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<publication102_Paper> getPublication102_papers() {
        return publication102_papers;
    }

    public void addPublication102_paper(Publication102_paper publication102_paper) {
        this.publication102_papers.add(publication102_paper);
    }
    public publication102_KnowledgeManager getPublication102_knowledgemanager() {
        return publication102_knowledgemanager;
    }

    public void setPublication102_knowledgemanager(publication102_KnowledgeManager publication102_knowledgemanager) {
        this.publication102_knowledgemanager = publication102_knowledgemanager;
    }

}