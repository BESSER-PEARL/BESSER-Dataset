





import java.util.List;
import java.util.ArrayList;

public class research18_Keyword extends Named {

    private String word;





    private research18_KnowledgeManager research18_knowledgemanager;


    public research18_Keyword(
        String word    ) {
        super(
        );
        this.word = word;
    }


    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public research18_KnowledgeManager getResearch18_knowledgemanager() {
        return research18_knowledgemanager;
    }

    public void setResearch18_knowledgemanager(research18_KnowledgeManager research18_knowledgemanager) {
        this.research18_knowledgemanager = research18_knowledgemanager;
    }

}