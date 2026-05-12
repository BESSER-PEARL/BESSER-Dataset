





import java.util.List;
import java.util.ArrayList;

public class research15_Collaboration  {

    private int ratio;





    private research15_Researcher research15_researcher;




    private research15_Paper research15_paper;


    public research15_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public research15_Researcher getResearch15_researcher() {
        return research15_researcher;
    }

    public void setResearch15_researcher(research15_Researcher research15_researcher) {
        this.research15_researcher = research15_researcher;
    }
    public research15_Paper getResearch15_paper() {
        return research15_paper;
    }

    public void setResearch15_paper(research15_Paper research15_paper) {
        this.research15_paper = research15_paper;
    }

}