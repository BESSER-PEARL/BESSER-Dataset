





import java.util.List;
import java.util.ArrayList;

public class research15_Keyword extends Named {

    private String description;





    private research15_KnowledgeManager research15_knowledgemanager;




    private research15_PaperKeyword research15_paperkeyword;




    private List<research15_Paper> research15_papers;


    public research15_Keyword(
        String description    ) {
        super(
        );
        this.description = description;
        this.research15_papers = new ArrayList<>();
    }

    public research15_Keyword(
        String description        ArrayList<research15_Paper> research15_papers    ) {
        this.description = description;
        this.research15_papers = research15_papers;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public research15_KnowledgeManager getResearch15_knowledgemanager() {
        return research15_knowledgemanager;
    }

    public void setResearch15_knowledgemanager(research15_KnowledgeManager research15_knowledgemanager) {
        this.research15_knowledgemanager = research15_knowledgemanager;
    }
    public research15_PaperKeyword getResearch15_paperkeyword() {
        return research15_paperkeyword;
    }

    public void setResearch15_paperkeyword(research15_PaperKeyword research15_paperkeyword) {
        this.research15_paperkeyword = research15_paperkeyword;
    }
    public List<research15_Paper> getResearch15_papers() {
        return research15_papers;
    }

    public void addResearch15_paper(Research15_paper research15_paper) {
        this.research15_papers.add(research15_paper);
    }

}