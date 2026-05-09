





import java.util.List;
import java.util.ArrayList;

public class research16_Write extends Labelled {

    private int timeSpent;





    private research16_Paragraph research16_paragraph;




    private research16_Researcher research16_researcher;


    public research16_Write(
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

    public research16_Paragraph getResearch16_paragraph() {
        return research16_paragraph;
    }

    public void setResearch16_paragraph(research16_Paragraph research16_paragraph) {
        this.research16_paragraph = research16_paragraph;
    }
    public research16_Researcher getResearch16_researcher() {
        return research16_researcher;
    }

    public void setResearch16_researcher(research16_Researcher research16_researcher) {
        this.research16_researcher = research16_researcher;
    }

}