





import java.util.List;
import java.util.ArrayList;

public class publication105_Collaboration  {

    private int ratio;





    private publication105_Researcher publication105_researcher;




    private publication105_Paper publication105_paper;


    public publication105_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public publication105_Researcher getPublication105_researcher() {
        return publication105_researcher;
    }

    public void setPublication105_researcher(publication105_Researcher publication105_researcher) {
        this.publication105_researcher = publication105_researcher;
    }
    public publication105_Paper getPublication105_paper() {
        return publication105_paper;
    }

    public void setPublication105_paper(publication105_Paper publication105_paper) {
        this.publication105_paper = publication105_paper;
    }

}