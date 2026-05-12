





import java.util.List;
import java.util.ArrayList;

public class publication103_Write extends Labelled {

    private int timeSpent;





    private publication103_Researcher publication103_researcher;


    public publication103_Write(
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

    public publication103_Researcher getPublication103_researcher() {
        return publication103_researcher;
    }

    public void setPublication103_researcher(publication103_Researcher publication103_researcher) {
        this.publication103_researcher = publication103_researcher;
    }

}