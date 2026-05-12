





import java.util.List;
import java.util.ArrayList;

public class research19_Write extends Labelled {

    private int timeSpent;





    private research19_Paragraph research19_paragraph;




    private research19_Researcher research19_researcher;


    public research19_Write(
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

    public research19_Paragraph getResearch19_paragraph() {
        return research19_paragraph;
    }

    public void setResearch19_paragraph(research19_Paragraph research19_paragraph) {
        this.research19_paragraph = research19_paragraph;
    }
    public research19_Researcher getResearch19_researcher() {
        return research19_researcher;
    }

    public void setResearch19_researcher(research19_Researcher research19_researcher) {
        this.research19_researcher = research19_researcher;
    }

}