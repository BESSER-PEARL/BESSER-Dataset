





import java.util.List;
import java.util.ArrayList;

public class research13_Write extends Labelled {

    private int timeSpent;





    private research13_Researcher research13_researcher;




    private research13_Paragraph research13_paragraph;


    public research13_Write(
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

    public research13_Researcher getResearch13_researcher() {
        return research13_researcher;
    }

    public void setResearch13_researcher(research13_Researcher research13_researcher) {
        this.research13_researcher = research13_researcher;
    }
    public research13_Paragraph getResearch13_paragraph() {
        return research13_paragraph;
    }

    public void setResearch13_paragraph(research13_Paragraph research13_paragraph) {
        this.research13_paragraph = research13_paragraph;
    }

}