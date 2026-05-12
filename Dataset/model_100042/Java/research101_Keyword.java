





import java.util.List;
import java.util.ArrayList;

public class research101_Keyword extends Named {

    private String description;





    private research101_KnowledgeManager research101_knowledgemanager;


    public research101_Keyword(
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

    public research101_KnowledgeManager getResearch101_knowledgemanager() {
        return research101_knowledgemanager;
    }

    public void setResearch101_knowledgemanager(research101_KnowledgeManager research101_knowledgemanager) {
        this.research101_knowledgemanager = research101_knowledgemanager;
    }

}