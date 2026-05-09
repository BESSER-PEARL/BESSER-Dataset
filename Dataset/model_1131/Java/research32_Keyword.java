





import java.util.List;
import java.util.ArrayList;

public class research32_Keyword extends Named {

    private String word;





    private List<research32_Paper> research32_papers;




    private research32_PaperKeyword research32_paperkeyword;




    private research32_KnowledgeManager research32_knowledgemanager;


    public research32_Keyword(
        String word    ) {
        super(
        );
        this.word = word;
        this.research32_papers = new ArrayList<>();
    }

    public research32_Keyword(
        String word        ArrayList<research32_Paper> research32_papers    ) {
        this.word = word;
        this.research32_papers = research32_papers;
    }

    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public List<research32_Paper> getResearch32_papers() {
        return research32_papers;
    }

    public void addResearch32_paper(Research32_paper research32_paper) {
        this.research32_papers.add(research32_paper);
    }
    public research32_PaperKeyword getResearch32_paperkeyword() {
        return research32_paperkeyword;
    }

    public void setResearch32_paperkeyword(research32_PaperKeyword research32_paperkeyword) {
        this.research32_paperkeyword = research32_paperkeyword;
    }
    public research32_KnowledgeManager getResearch32_knowledgemanager() {
        return research32_knowledgemanager;
    }

    public void setResearch32_knowledgemanager(research32_KnowledgeManager research32_knowledgemanager) {
        this.research32_knowledgemanager = research32_knowledgemanager;
    }

}