





import java.util.List;
import java.util.ArrayList;

public class research16_Collaboration  {

    private int ratio;





    private research16_Researcher research16_researcher;




    private research16_Paper research16_paper;


    public research16_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public research16_Researcher getResearch16_researcher() {
        return research16_researcher;
    }

    public void setResearch16_researcher(research16_Researcher research16_researcher) {
        this.research16_researcher = research16_researcher;
    }
    public research16_Paper getResearch16_paper() {
        return research16_paper;
    }

    public void setResearch16_paper(research16_Paper research16_paper) {
        this.research16_paper = research16_paper;
    }

}