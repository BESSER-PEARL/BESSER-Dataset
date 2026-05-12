





import java.util.List;
import java.util.ArrayList;

public class research32_Collaboration  {

    private int ratio;





    private research32_Researcher research32_researcher;




    private research32_Paper research32_paper;


    public research32_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public research32_Researcher getResearch32_researcher() {
        return research32_researcher;
    }

    public void setResearch32_researcher(research32_Researcher research32_researcher) {
        this.research32_researcher = research32_researcher;
    }
    public research32_Paper getResearch32_paper() {
        return research32_paper;
    }

    public void setResearch32_paper(research32_Paper research32_paper) {
        this.research32_paper = research32_paper;
    }

}