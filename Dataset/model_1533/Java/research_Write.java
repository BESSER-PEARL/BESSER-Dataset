





import java.util.List;
import java.util.ArrayList;

public class research_Write extends Labelled {

    private int timeSpent;





    private research_Researcher research_researcher;


    public research_Write(
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

    public research_Researcher getResearch_researcher() {
        return research_researcher;
    }

    public void setResearch_researcher(research_Researcher research_researcher) {
        this.research_researcher = research_researcher;
    }

}