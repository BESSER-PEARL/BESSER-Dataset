





import java.util.List;
import java.util.ArrayList;

public class research15_Write extends Labelled {

    private int timeSpent;





    private research15_Paragraph research15_paragraph;




    private research15_Researcher research15_researcher;


    public research15_Write(
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

    public research15_Paragraph getResearch15_paragraph() {
        return research15_paragraph;
    }

    public void setResearch15_paragraph(research15_Paragraph research15_paragraph) {
        this.research15_paragraph = research15_paragraph;
    }
    public research15_Researcher getResearch15_researcher() {
        return research15_researcher;
    }

    public void setResearch15_researcher(research15_Researcher research15_researcher) {
        this.research15_researcher = research15_researcher;
    }

}