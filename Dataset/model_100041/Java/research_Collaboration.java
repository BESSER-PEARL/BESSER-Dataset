





import java.util.List;
import java.util.ArrayList;

public class research_Collaboration  {

    private int ratio;





    private research_Researcher research_researcher;




    private research_Paper research_paper;


    public research_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public research_Researcher getResearch_researcher() {
        return research_researcher;
    }

    public void setResearch_researcher(research_Researcher research_researcher) {
        this.research_researcher = research_researcher;
    }
    public research_Paper getResearch_paper() {
        return research_paper;
    }

    public void setResearch_paper(research_Paper research_paper) {
        this.research_paper = research_paper;
    }

}