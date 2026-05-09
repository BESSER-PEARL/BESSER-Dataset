





import java.util.List;
import java.util.ArrayList;

public class research23_Keyword extends Named {

    private String word;





    private research23_KnowledgeManager research23_knowledgemanager;


    public research23_Keyword(
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

    public research23_KnowledgeManager getResearch23_knowledgemanager() {
        return research23_knowledgemanager;
    }

    public void setResearch23_knowledgemanager(research23_KnowledgeManager research23_knowledgemanager) {
        this.research23_knowledgemanager = research23_knowledgemanager;
    }

}