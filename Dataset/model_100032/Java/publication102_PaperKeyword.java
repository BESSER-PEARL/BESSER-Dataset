





import java.util.List;
import java.util.ArrayList;

public class publication102_PaperKeyword  {

    private int weight;





    private publication102_Paper publication102_paper;




    private publication102_Keyword publication102_keyword;


    public publication102_PaperKeyword(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public publication102_Paper getPublication102_paper() {
        return publication102_paper;
    }

    public void setPublication102_paper(publication102_Paper publication102_paper) {
        this.publication102_paper = publication102_paper;
    }
    public publication102_Keyword getPublication102_keyword() {
        return publication102_keyword;
    }

    public void setPublication102_keyword(publication102_Keyword publication102_keyword) {
        this.publication102_keyword = publication102_keyword;
    }

}