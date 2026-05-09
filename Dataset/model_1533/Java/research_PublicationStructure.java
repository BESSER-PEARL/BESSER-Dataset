





import java.util.List;
import java.util.ArrayList;

public class research_PublicationStructure extends Named {






    private List<research_Researcher> research_researchers;




    private research_KnowledgeManager research_knowledgemanager;




    private List<research_Paper> research_papers;


    public research_PublicationStructure(
    ) {
        super(
        );
        this.research_researchers = new ArrayList<>();
        this.research_papers = new ArrayList<>();
    }

    public research_PublicationStructure(
        ArrayList<research_Researcher> research_researchers,        ArrayList<research_Paper> research_papers    ) {
        this.research_researchers = research_researchers;
        this.research_papers = research_papers;
    }


    public List<research_Researcher> getResearch_researchers() {
        return research_researchers;
    }

    public void addResearch_researcher(Research_researcher research_researcher) {
        this.research_researchers.add(research_researcher);
    }
    public research_KnowledgeManager getResearch_knowledgemanager() {
        return research_knowledgemanager;
    }

    public void setResearch_knowledgemanager(research_KnowledgeManager research_knowledgemanager) {
        this.research_knowledgemanager = research_knowledgemanager;
    }
    public List<research_Paper> getResearch_papers() {
        return research_papers;
    }

    public void addResearch_paper(Research_paper research_paper) {
        this.research_papers.add(research_paper);
    }

}