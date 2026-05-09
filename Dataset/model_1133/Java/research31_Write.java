





import java.util.List;
import java.util.ArrayList;

public class research31_Write extends Labelled {

    private int timeSpent;





    private research31_Paragraph research31_paragraph;




    private research31_Researcher research31_researcher;


    public research31_Write(
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

    public research31_Paragraph getResearch31_paragraph() {
        return research31_paragraph;
    }

    public void setResearch31_paragraph(research31_Paragraph research31_paragraph) {
        this.research31_paragraph = research31_paragraph;
    }
    public research31_Researcher getResearch31_researcher() {
        return research31_researcher;
    }

    public void setResearch31_researcher(research31_Researcher research31_researcher) {
        this.research31_researcher = research31_researcher;
    }

}