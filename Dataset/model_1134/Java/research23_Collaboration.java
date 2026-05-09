





import java.util.List;
import java.util.ArrayList;

public class research23_Collaboration  {

    private int ratio;





    private research23_Paper research23_paper;




    private research23_Researcher research23_researcher;


    public research23_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public research23_Paper getResearch23_paper() {
        return research23_paper;
    }

    public void setResearch23_paper(research23_Paper research23_paper) {
        this.research23_paper = research23_paper;
    }
    public research23_Researcher getResearch23_researcher() {
        return research23_researcher;
    }

    public void setResearch23_researcher(research23_Researcher research23_researcher) {
        this.research23_researcher = research23_researcher;
    }

}