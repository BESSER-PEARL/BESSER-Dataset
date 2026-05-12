





import java.util.List;
import java.util.ArrayList;

public class research23_Write extends Labelled {

    private int timeSpent;





    private research23_Researcher research23_researcher;




    private research23_Paragraph research23_paragraph;


    public research23_Write(
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

    public research23_Researcher getResearch23_researcher() {
        return research23_researcher;
    }

    public void setResearch23_researcher(research23_Researcher research23_researcher) {
        this.research23_researcher = research23_researcher;
    }
    public research23_Paragraph getResearch23_paragraph() {
        return research23_paragraph;
    }

    public void setResearch23_paragraph(research23_Paragraph research23_paragraph) {
        this.research23_paragraph = research23_paragraph;
    }

}