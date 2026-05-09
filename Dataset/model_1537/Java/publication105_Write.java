





import java.util.List;
import java.util.ArrayList;

public class publication105_Write extends Labelled {

    private int timeSpent;





    private publication105_Paragraph publication105_paragraph;




    private publication105_Researcher publication105_researcher;


    public publication105_Write(
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

    public publication105_Paragraph getPublication105_paragraph() {
        return publication105_paragraph;
    }

    public void setPublication105_paragraph(publication105_Paragraph publication105_paragraph) {
        this.publication105_paragraph = publication105_paragraph;
    }
    public publication105_Researcher getPublication105_researcher() {
        return publication105_researcher;
    }

    public void setPublication105_researcher(publication105_Researcher publication105_researcher) {
        this.publication105_researcher = publication105_researcher;
    }

}