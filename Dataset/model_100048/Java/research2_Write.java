





import java.util.List;
import java.util.ArrayList;

public class research2_Write extends Labelled {

    private int timeSpent;





    private research2_Researcher research2_researcher;




    private research2_Paragraph research2_paragraph;


    public research2_Write(
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

    public research2_Researcher getResearch2_researcher() {
        return research2_researcher;
    }

    public void setResearch2_researcher(research2_Researcher research2_researcher) {
        this.research2_researcher = research2_researcher;
    }
    public research2_Paragraph getResearch2_paragraph() {
        return research2_paragraph;
    }

    public void setResearch2_paragraph(research2_Paragraph research2_paragraph) {
        this.research2_paragraph = research2_paragraph;
    }

}