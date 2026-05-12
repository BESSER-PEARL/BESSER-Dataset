





import java.util.List;
import java.util.ArrayList;

public class research19_PublicationStructure extends Named {






    private List<research19_Paper> research19_papers;




    private research19_PublicationSystem research19_publicationsystem;




    private research19_KnowledgeManager research19_knowledgemanager;


    public research19_PublicationStructure(
    ) {
        super(
        );
        this.research19_papers = new ArrayList<>();
    }

    public research19_PublicationStructure(
        ArrayList<research19_Paper> research19_papers    ) {
        this.research19_papers = research19_papers;
    }


    public List<research19_Paper> getResearch19_papers() {
        return research19_papers;
    }

    public void addResearch19_paper(Research19_paper research19_paper) {
        this.research19_papers.add(research19_paper);
    }
    public research19_PublicationSystem getResearch19_publicationsystem() {
        return research19_publicationsystem;
    }

    public void setResearch19_publicationsystem(research19_PublicationSystem research19_publicationsystem) {
        this.research19_publicationsystem = research19_publicationsystem;
    }
    public research19_KnowledgeManager getResearch19_knowledgemanager() {
        return research19_knowledgemanager;
    }

    public void setResearch19_knowledgemanager(research19_KnowledgeManager research19_knowledgemanager) {
        this.research19_knowledgemanager = research19_knowledgemanager;
    }

}