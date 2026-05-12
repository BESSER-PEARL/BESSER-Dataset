





import java.util.List;
import java.util.ArrayList;

public class publication101_Collaboration  {

    private int ratio;





    private publication101_Researcher publication101_researcher;




    private publication101_Paper publication101_paper;


    public publication101_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public publication101_Researcher getPublication101_researcher() {
        return publication101_researcher;
    }

    public void setPublication101_researcher(publication101_Researcher publication101_researcher) {
        this.publication101_researcher = publication101_researcher;
    }
    public publication101_Paper getPublication101_paper() {
        return publication101_paper;
    }

    public void setPublication101_paper(publication101_Paper publication101_paper) {
        this.publication101_paper = publication101_paper;
    }

}