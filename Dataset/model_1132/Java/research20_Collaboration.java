





import java.util.List;
import java.util.ArrayList;

public class research20_Collaboration  {

    private int ratio;





    private research20_Paper research20_paper;




    private research20_Researcher research20_researcher;


    public research20_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public research20_Paper getResearch20_paper() {
        return research20_paper;
    }

    public void setResearch20_paper(research20_Paper research20_paper) {
        this.research20_paper = research20_paper;
    }
    public research20_Researcher getResearch20_researcher() {
        return research20_researcher;
    }

    public void setResearch20_researcher(research20_Researcher research20_researcher) {
        this.research20_researcher = research20_researcher;
    }

}