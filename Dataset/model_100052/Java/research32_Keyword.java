





import java.util.List;
import java.util.ArrayList;

public class research32_Keyword extends Named {

    private String word;





    private research32_KnowledgeManager research32_knowledgemanager;


    public research32_Keyword(
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

    public research32_KnowledgeManager getResearch32_knowledgemanager() {
        return research32_knowledgemanager;
    }

    public void setResearch32_knowledgemanager(research32_KnowledgeManager research32_knowledgemanager) {
        this.research32_knowledgemanager = research32_knowledgemanager;
    }

}