





import java.util.List;
import java.util.ArrayList;

public class research20_Keyword extends Named {

    private String word;





    private List<research20_Paper> research20_papers;




    private research20_KnowledgeManager research20_knowledgemanager;


    public research20_Keyword(
        String word    ) {
        super(
        );
        this.word = word;
        this.research20_papers = new ArrayList<>();
    }

    public research20_Keyword(
        String word        ArrayList<research20_Paper> research20_papers    ) {
        this.word = word;
        this.research20_papers = research20_papers;
    }

    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public List<research20_Paper> getResearch20_papers() {
        return research20_papers;
    }

    public void addResearch20_paper(Research20_paper research20_paper) {
        this.research20_papers.add(research20_paper);
    }
    public research20_KnowledgeManager getResearch20_knowledgemanager() {
        return research20_knowledgemanager;
    }

    public void setResearch20_knowledgemanager(research20_KnowledgeManager research20_knowledgemanager) {
        this.research20_knowledgemanager = research20_knowledgemanager;
    }

}