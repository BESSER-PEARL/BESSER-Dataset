





import java.util.List;
import java.util.ArrayList;

public class research18_Collaboration  {

    private int ratio;





    private research18_Researcher research18_researcher;




    private research18_Paper research18_paper;


    public research18_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public research18_Researcher getResearch18_researcher() {
        return research18_researcher;
    }

    public void setResearch18_researcher(research18_Researcher research18_researcher) {
        this.research18_researcher = research18_researcher;
    }
    public research18_Paper getResearch18_paper() {
        return research18_paper;
    }

    public void setResearch18_paper(research18_Paper research18_paper) {
        this.research18_paper = research18_paper;
    }

}