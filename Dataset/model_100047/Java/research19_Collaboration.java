





import java.util.List;
import java.util.ArrayList;

public class research19_Collaboration  {

    private int ratio;





    private research19_Researcher research19_researcher;




    private research19_Paper research19_paper;


    public research19_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public research19_Researcher getResearch19_researcher() {
        return research19_researcher;
    }

    public void setResearch19_researcher(research19_Researcher research19_researcher) {
        this.research19_researcher = research19_researcher;
    }
    public research19_Paper getResearch19_paper() {
        return research19_paper;
    }

    public void setResearch19_paper(research19_Paper research19_paper) {
        this.research19_paper = research19_paper;
    }

}