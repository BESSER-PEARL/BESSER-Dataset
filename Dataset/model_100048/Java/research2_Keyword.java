





import java.util.List;
import java.util.ArrayList;

public class research2_Keyword extends Named {

    private String description;





    private research2_Paper research2_paper;




    private research2_KnowledgeManager research2_knowledgemanager;




    private List<research2_Paper> research2_papers;


    public research2_Keyword(
        String description    ) {
        super(
        );
        this.description = description;
        this.research2_papers = new ArrayList<>();
    }

    public research2_Keyword(
        String description        ArrayList<research2_Paper> research2_papers    ) {
        this.description = description;
        this.research2_papers = research2_papers;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public research2_Paper getResearch2_paper() {
        return research2_paper;
    }

    public void setResearch2_paper(research2_Paper research2_paper) {
        this.research2_paper = research2_paper;
    }
    public research2_KnowledgeManager getResearch2_knowledgemanager() {
        return research2_knowledgemanager;
    }

    public void setResearch2_knowledgemanager(research2_KnowledgeManager research2_knowledgemanager) {
        this.research2_knowledgemanager = research2_knowledgemanager;
    }
    public List<research2_Paper> getResearch2_papers() {
        return research2_papers;
    }

    public void addResearch2_paper(Research2_paper research2_paper) {
        this.research2_papers.add(research2_paper);
    }

}