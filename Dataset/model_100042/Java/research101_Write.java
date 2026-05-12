





import java.util.List;
import java.util.ArrayList;

public class research101_Write extends Labelled {

    private int timeSpent;





    private research101_Paragraph research101_paragraph;




    private research101_Researcher research101_researcher;


    public research101_Write(
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

    public research101_Paragraph getResearch101_paragraph() {
        return research101_paragraph;
    }

    public void setResearch101_paragraph(research101_Paragraph research101_paragraph) {
        this.research101_paragraph = research101_paragraph;
    }
    public research101_Researcher getResearch101_researcher() {
        return research101_researcher;
    }

    public void setResearch101_researcher(research101_Researcher research101_researcher) {
        this.research101_researcher = research101_researcher;
    }

}