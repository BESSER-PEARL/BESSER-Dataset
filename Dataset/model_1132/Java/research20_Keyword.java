





import java.util.List;
import java.util.ArrayList;

public class research20_Keyword extends Named {

    private String word;





    private research20_KnowledgeManager research20_knowledgemanager;


    public research20_Keyword(
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

    public research20_KnowledgeManager getResearch20_knowledgemanager() {
        return research20_knowledgemanager;
    }

    public void setResearch20_knowledgemanager(research20_KnowledgeManager research20_knowledgemanager) {
        this.research20_knowledgemanager = research20_knowledgemanager;
    }

}