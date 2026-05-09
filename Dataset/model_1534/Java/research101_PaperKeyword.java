





import java.util.List;
import java.util.ArrayList;

public class research101_PaperKeyword  {

    private int weight;





    private research101_Keyword research101_keyword;




    private research101_Paper research101_paper;


    public research101_PaperKeyword(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public research101_Keyword getResearch101_keyword() {
        return research101_keyword;
    }

    public void setResearch101_keyword(research101_Keyword research101_keyword) {
        this.research101_keyword = research101_keyword;
    }
    public research101_Paper getResearch101_paper() {
        return research101_paper;
    }

    public void setResearch101_paper(research101_Paper research101_paper) {
        this.research101_paper = research101_paper;
    }

}