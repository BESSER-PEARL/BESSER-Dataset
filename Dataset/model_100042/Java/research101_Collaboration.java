





import java.util.List;
import java.util.ArrayList;

public class research101_Collaboration  {

    private int ratio;





    private research101_Researcher research101_researcher;




    private research101_Paper research101_paper;


    public research101_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public research101_Researcher getResearch101_researcher() {
        return research101_researcher;
    }

    public void setResearch101_researcher(research101_Researcher research101_researcher) {
        this.research101_researcher = research101_researcher;
    }
    public research101_Paper getResearch101_paper() {
        return research101_paper;
    }

    public void setResearch101_paper(research101_Paper research101_paper) {
        this.research101_paper = research101_paper;
    }

}