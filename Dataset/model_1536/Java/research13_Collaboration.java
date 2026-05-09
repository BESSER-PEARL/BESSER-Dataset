





import java.util.List;
import java.util.ArrayList;

public class research13_Collaboration  {

    private int ratio;





    private research13_Paper research13_paper;




    private research13_Researcher research13_researcher;


    public research13_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public research13_Paper getResearch13_paper() {
        return research13_paper;
    }

    public void setResearch13_paper(research13_Paper research13_paper) {
        this.research13_paper = research13_paper;
    }
    public research13_Researcher getResearch13_researcher() {
        return research13_researcher;
    }

    public void setResearch13_researcher(research13_Researcher research13_researcher) {
        this.research13_researcher = research13_researcher;
    }

}