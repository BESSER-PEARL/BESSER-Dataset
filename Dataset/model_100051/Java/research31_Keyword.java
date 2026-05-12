





import java.util.List;
import java.util.ArrayList;

public class research31_Keyword extends Named {

    private String word;





    private research31_KnowledgeManager research31_knowledgemanager;




    private research31_PaperKeyword research31_paperkeyword;


    public research31_Keyword(
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

    public research31_KnowledgeManager getResearch31_knowledgemanager() {
        return research31_knowledgemanager;
    }

    public void setResearch31_knowledgemanager(research31_KnowledgeManager research31_knowledgemanager) {
        this.research31_knowledgemanager = research31_knowledgemanager;
    }
    public research31_PaperKeyword getResearch31_paperkeyword() {
        return research31_paperkeyword;
    }

    public void setResearch31_paperkeyword(research31_PaperKeyword research31_paperkeyword) {
        this.research31_paperkeyword = research31_paperkeyword;
    }

}