





import java.util.List;
import java.util.ArrayList;

public class research18_Write extends Labelled {

    private int timeSpent;





    private research18_Researcher research18_researcher;




    private research18_Paragraph research18_paragraph;


    public research18_Write(
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

    public research18_Researcher getResearch18_researcher() {
        return research18_researcher;
    }

    public void setResearch18_researcher(research18_Researcher research18_researcher) {
        this.research18_researcher = research18_researcher;
    }
    public research18_Paragraph getResearch18_paragraph() {
        return research18_paragraph;
    }

    public void setResearch18_paragraph(research18_Paragraph research18_paragraph) {
        this.research18_paragraph = research18_paragraph;
    }

}