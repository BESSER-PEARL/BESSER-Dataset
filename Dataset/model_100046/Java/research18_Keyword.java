





import java.util.List;
import java.util.ArrayList;

public class research18_Keyword extends Named {

    private String word;





    private List<research18_Paper> research18_papers;




    private research18_KnowledgeManager research18_knowledgemanager;


    public research18_Keyword(
        String word    ) {
        super(
        );
        this.word = word;
        this.research18_papers = new ArrayList<>();
    }

    public research18_Keyword(
        String word        ArrayList<research18_Paper> research18_papers    ) {
        this.word = word;
        this.research18_papers = research18_papers;
    }

    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public List<research18_Paper> getResearch18_papers() {
        return research18_papers;
    }

    public void addResearch18_paper(Research18_paper research18_paper) {
        this.research18_papers.add(research18_paper);
    }
    public research18_KnowledgeManager getResearch18_knowledgemanager() {
        return research18_knowledgemanager;
    }

    public void setResearch18_knowledgemanager(research18_KnowledgeManager research18_knowledgemanager) {
        this.research18_knowledgemanager = research18_knowledgemanager;
    }

}