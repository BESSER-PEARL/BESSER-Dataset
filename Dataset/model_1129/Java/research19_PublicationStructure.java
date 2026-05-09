





import java.util.List;
import java.util.ArrayList;

public class research19_PublicationStructure extends Named {






    private List<research19_Researcher> research19_researchers;




    private research19_KnowledgeManager research19_knowledgemanager;




    private List<research19_Paper> research19_papers;




    private research19_PublicationSystem research19_publicationsystem;


    public research19_PublicationStructure(
    ) {
        super(
        );
        this.research19_researchers = new ArrayList<>();
        this.research19_papers = new ArrayList<>();
    }

    public research19_PublicationStructure(
        ArrayList<research19_Researcher> research19_researchers,        ArrayList<research19_Paper> research19_papers    ) {
        this.research19_researchers = research19_researchers;
        this.research19_papers = research19_papers;
    }


    public List<research19_Researcher> getResearch19_researchers() {
        return research19_researchers;
    }

    public void addResearch19_researcher(Research19_researcher research19_researcher) {
        this.research19_researchers.add(research19_researcher);
    }
    public research19_KnowledgeManager getResearch19_knowledgemanager() {
        return research19_knowledgemanager;
    }

    public void setResearch19_knowledgemanager(research19_KnowledgeManager research19_knowledgemanager) {
        this.research19_knowledgemanager = research19_knowledgemanager;
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

}