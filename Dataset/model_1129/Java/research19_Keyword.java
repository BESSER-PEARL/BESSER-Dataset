





import java.util.List;
import java.util.ArrayList;

public class research19_Keyword extends Named {

    private String word;





    private List<research19_Paper> research19_papers;


    public research19_Keyword(
        String word    ) {
        super(
        );
        this.word = word;
        this.research19_papers = new ArrayList<>();
    }

    public research19_Keyword(
        String word        ArrayList<research19_Paper> research19_papers    ) {
        this.word = word;
        this.research19_papers = research19_papers;
    }

    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public List<research19_Paper> getResearch19_papers() {
        return research19_papers;
    }

    public void addResearch19_paper(Research19_paper research19_paper) {
        this.research19_papers.add(research19_paper);
    }

}