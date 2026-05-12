





import java.util.List;
import java.util.ArrayList;

public class research16_Keyword extends Named {

    private String word;





    private research16_KnowledgeManager research16_knowledgemanager;




    private List<research16_Paper> research16_papers;


    public research16_Keyword(
        String word    ) {
        super(
        );
        this.word = word;
        this.research16_papers = new ArrayList<>();
    }

    public research16_Keyword(
        String word        ArrayList<research16_Paper> research16_papers    ) {
        this.word = word;
        this.research16_papers = research16_papers;
    }

    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public research16_KnowledgeManager getResearch16_knowledgemanager() {
        return research16_knowledgemanager;
    }

    public void setResearch16_knowledgemanager(research16_KnowledgeManager research16_knowledgemanager) {
        this.research16_knowledgemanager = research16_knowledgemanager;
    }
    public List<research16_Paper> getResearch16_papers() {
        return research16_papers;
    }

    public void addResearch16_paper(Research16_paper research16_paper) {
        this.research16_papers.add(research16_paper);
    }

}