





import java.util.List;
import java.util.ArrayList;

public class research32_PublicationStructure extends Named {






    private List<research32_Paper> research32_papers;




    private research32_PublicationSystem research32_publicationsystem;




    private research32_KnowledgeManager research32_knowledgemanager;


    public research32_PublicationStructure(
    ) {
        super(
        );
        this.research32_papers = new ArrayList<>();
    }

    public research32_PublicationStructure(
        ArrayList<research32_Paper> research32_papers    ) {
        this.research32_papers = research32_papers;
    }


    public List<research32_Paper> getResearch32_papers() {
        return research32_papers;
    }

    public void addResearch32_paper(Research32_paper research32_paper) {
        this.research32_papers.add(research32_paper);
    }
    public research32_PublicationSystem getResearch32_publicationsystem() {
        return research32_publicationsystem;
    }

    public void setResearch32_publicationsystem(research32_PublicationSystem research32_publicationsystem) {
        this.research32_publicationsystem = research32_publicationsystem;
    }
    public research32_KnowledgeManager getResearch32_knowledgemanager() {
        return research32_knowledgemanager;
    }

    public void setResearch32_knowledgemanager(research32_KnowledgeManager research32_knowledgemanager) {
        this.research32_knowledgemanager = research32_knowledgemanager;
    }

}