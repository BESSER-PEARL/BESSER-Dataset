





import java.util.List;
import java.util.ArrayList;

public class tp6_PaperKeywords  {

    private int weight;





    private tp6_Keyword tp6_keyword;




    private tp6_Paper tp6_paper;


    public tp6_PaperKeywords(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public tp6_Keyword getTp6_keyword() {
        return tp6_keyword;
    }

    public void setTp6_keyword(tp6_Keyword tp6_keyword) {
        this.tp6_keyword = tp6_keyword;
    }
    public tp6_Paper getTp6_paper() {
        return tp6_paper;
    }

    public void setTp6_paper(tp6_Paper tp6_paper) {
        this.tp6_paper = tp6_paper;
    }

}