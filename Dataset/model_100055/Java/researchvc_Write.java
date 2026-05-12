





import java.util.List;
import java.util.ArrayList;

public class researchvc_Write extends Labelled {

    private int timeSpent;





    private researchvc_Researcher researchvc_researcher;


    public researchvc_Write(
        int timeSpent    ) {
        super(
        );
        this.timeSpent = timeSpent;
    }


    public int getTimespent() {
        return timeSpent;
    }

    public void setTimespent(int timeSpent) {
        this.timeSpent = timeSpent;
    }

    public researchvc_Researcher getResearchvc_researcher() {
        return researchvc_researcher;
    }

    public void setResearchvc_researcher(researchvc_Researcher researchvc_researcher) {
        this.researchvc_researcher = researchvc_researcher;
    }

}