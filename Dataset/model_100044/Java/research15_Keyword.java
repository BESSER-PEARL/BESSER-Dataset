





import java.util.List;
import java.util.ArrayList;

public class research15_Keyword extends Named {

    private String description;





    private research15_KnowledgeManager research15_knowledgemanager;


    public research15_Keyword(
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

    public research15_KnowledgeManager getResearch15_knowledgemanager() {
        return research15_knowledgemanager;
    }

    public void setResearch15_knowledgemanager(research15_KnowledgeManager research15_knowledgemanager) {
        this.research15_knowledgemanager = research15_knowledgemanager;
    }

}