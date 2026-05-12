





import java.util.List;
import java.util.ArrayList;

public class research_Keyword extends Named {

    private String description;





    private research_KnowledgeManager research_knowledgemanager;


    public research_Keyword(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public research_KnowledgeManager getResearch_knowledgemanager() {
        return research_knowledgemanager;
    }

    public void setResearch_knowledgemanager(research_KnowledgeManager research_knowledgemanager) {
        this.research_knowledgemanager = research_knowledgemanager;
    }

}