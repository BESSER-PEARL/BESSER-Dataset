





import java.util.List;
import java.util.ArrayList;

public class tp5_Collaboration  {

    private int ratio;





    private tp5_Researcher tp5_researcher;




    private tp5_Paper tp5_paper;


    public tp5_Collaboration(
        int ratio    ) {
        this.ratio = ratio;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }

    public tp5_Researcher getTp5_researcher() {
        return tp5_researcher;
    }

    public void setTp5_researcher(tp5_Researcher tp5_researcher) {
        this.tp5_researcher = tp5_researcher;
    }
    public tp5_Paper getTp5_paper() {
        return tp5_paper;
    }

    public void setTp5_paper(tp5_Paper tp5_paper) {
        this.tp5_paper = tp5_paper;
    }

}