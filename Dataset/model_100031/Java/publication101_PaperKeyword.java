





import java.util.List;
import java.util.ArrayList;

public class publication101_PaperKeyword  {

    private int weight;





    private publication101_Keyword publication101_keyword;




    private publication101_Paper publication101_paper;


    public publication101_PaperKeyword(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public publication101_Keyword getPublication101_keyword() {
        return publication101_keyword;
    }

    public void setPublication101_keyword(publication101_Keyword publication101_keyword) {
        this.publication101_keyword = publication101_keyword;
    }
    public publication101_Paper getPublication101_paper() {
        return publication101_paper;
    }

    public void setPublication101_paper(publication101_Paper publication101_paper) {
        this.publication101_paper = publication101_paper;
    }

}