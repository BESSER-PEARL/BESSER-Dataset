





import java.util.List;
import java.util.ArrayList;

public class research_PaperKeyword  {

    private int weight;





    private research_Paper research_paper;




    private research_Keyword research_keyword;


    public research_PaperKeyword(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public research_Paper getResearch_paper() {
        return research_paper;
    }

    public void setResearch_paper(research_Paper research_paper) {
        this.research_paper = research_paper;
    }
    public research_Keyword getResearch_keyword() {
        return research_keyword;
    }

    public void setResearch_keyword(research_Keyword research_keyword) {
        this.research_keyword = research_keyword;
    }

}