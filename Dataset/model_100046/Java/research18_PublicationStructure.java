





import java.util.List;
import java.util.ArrayList;

public class research18_PublicationStructure extends Named {






    private research18_PublicationSystem research18_publicationsystem;




    private List<research18_Paper> research18_papers;




    private research18_KnowledgeManager research18_knowledgemanager;


    public research18_PublicationStructure(
    ) {
        super(
        );
        this.research18_papers = new ArrayList<>();
    }

    public research18_PublicationStructure(
        ArrayList<research18_Paper> research18_papers    ) {
        this.research18_papers = research18_papers;
    }


    public research18_PublicationSystem getResearch18_publicationsystem() {
        return research18_publicationsystem;
    }

    public void setResearch18_publicationsystem(research18_PublicationSystem research18_publicationsystem) {
        this.research18_publicationsystem = research18_publicationsystem;
    }
    public List<research18_Paper> getResearch18_papers() {
        return research18_papers;
    }

    public void addResearch18_paper(Research18_paper research18_paper) {
        this.research18_papers.add(research18_paper);
    }
    public research18_KnowledgeManager getResearch18_knowledgemanager() {
        return research18_knowledgemanager;
    }

    public void setResearch18_knowledgemanager(research18_KnowledgeManager research18_knowledgemanager) {
        this.research18_knowledgemanager = research18_knowledgemanager;
    }

}