





import java.util.List;
import java.util.ArrayList;

public class publication101_Write extends Labelled {

    private int timeSpent;





    private publication101_Paragraph publication101_paragraph;




    private publication101_Researcher publication101_researcher;


    public publication101_Write(
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

    public publication101_Paragraph getPublication101_paragraph() {
        return publication101_paragraph;
    }

    public void setPublication101_paragraph(publication101_Paragraph publication101_paragraph) {
        this.publication101_paragraph = publication101_paragraph;
    }
    public publication101_Researcher getPublication101_researcher() {
        return publication101_researcher;
    }

    public void setPublication101_researcher(publication101_Researcher publication101_researcher) {
        this.publication101_researcher = publication101_researcher;
    }

}