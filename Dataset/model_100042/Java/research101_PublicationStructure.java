





import java.util.List;
import java.util.ArrayList;

public class research101_PublicationStructure extends Named {






    private List<research101_Paper> research101_papers;




    private research101_KnowledgeManager research101_knowledgemanager;




    private research101_PublicationSystem research101_publicationsystem;


    public research101_PublicationStructure(
    ) {
        super(
        );
        this.research101_papers = new ArrayList<>();
    }

    public research101_PublicationStructure(
        ArrayList<research101_Paper> research101_papers    ) {
        this.research101_papers = research101_papers;
    }


    public List<research101_Paper> getResearch101_papers() {
        return research101_papers;
    }

    public void addResearch101_paper(Research101_paper research101_paper) {
        this.research101_papers.add(research101_paper);
    }
    public research101_KnowledgeManager getResearch101_knowledgemanager() {
        return research101_knowledgemanager;
    }

    public void setResearch101_knowledgemanager(research101_KnowledgeManager research101_knowledgemanager) {
        this.research101_knowledgemanager = research101_knowledgemanager;
    }
    public research101_PublicationSystem getResearch101_publicationsystem() {
        return research101_publicationsystem;
    }

    public void setResearch101_publicationsystem(research101_PublicationSystem research101_publicationsystem) {
        this.research101_publicationsystem = research101_publicationsystem;
    }

}