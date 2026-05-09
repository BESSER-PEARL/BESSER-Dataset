





import java.util.List;
import java.util.ArrayList;

public class research20_Write extends Labelled {

    private int timeSpent;





    private research20_Paragraph research20_paragraph;




    private research20_Researcher research20_researcher;


    public research20_Write(
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

    public research20_Paragraph getResearch20_paragraph() {
        return research20_paragraph;
    }

    public void setResearch20_paragraph(research20_Paragraph research20_paragraph) {
        this.research20_paragraph = research20_paragraph;
    }
    public research20_Researcher getResearch20_researcher() {
        return research20_researcher;
    }

    public void setResearch20_researcher(research20_Researcher research20_researcher) {
        this.research20_researcher = research20_researcher;
    }

}