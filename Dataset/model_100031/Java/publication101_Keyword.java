





import java.util.List;
import java.util.ArrayList;

public class publication101_Keyword extends Named {

    private String description;





    private publication101_KnowledgeManager publication101_knowledgemanager;


    public publication101_Keyword(
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

    public publication101_KnowledgeManager getPublication101_knowledgemanager() {
        return publication101_knowledgemanager;
    }

    public void setPublication101_knowledgemanager(publication101_KnowledgeManager publication101_knowledgemanager) {
        this.publication101_knowledgemanager = publication101_knowledgemanager;
    }

}