





import java.util.List;
import java.util.ArrayList;

public class publication102_Collaboration  {

    private int ratio;





    private publication102_Paper publication102_paper;




    private publication102_Researcher publication102_researcher;


    public publication102_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public publication102_Paper getPublication102_paper() {
        return publication102_paper;
    }

    public void setPublication102_paper(publication102_Paper publication102_paper) {
        this.publication102_paper = publication102_paper;
    }
    public publication102_Researcher getPublication102_researcher() {
        return publication102_researcher;
    }

    public void setPublication102_researcher(publication102_Researcher publication102_researcher) {
        this.publication102_researcher = publication102_researcher;
    }

}