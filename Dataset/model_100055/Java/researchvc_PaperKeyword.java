





import java.util.List;
import java.util.ArrayList;

public class researchvc_PaperKeyword  {

    private int weight;





    private researchvc_Paper researchvc_paper;


    public researchvc_PaperKeyword(
        int weight    ) {
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }

    public researchvc_Paper getResearchvc_paper() {
        return researchvc_paper;
    }

    public void setResearchvc_paper(researchvc_Paper researchvc_paper) {
        this.researchvc_paper = researchvc_paper;
    }

}