





import java.util.List;
import java.util.ArrayList;

public class research32_Write extends Labelled {

    private int timeSpent;





    private research32_Researcher research32_researcher;




    private research32_Paragraph research32_paragraph;


    public research32_Write(
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

    public research32_Researcher getResearch32_researcher() {
        return research32_researcher;
    }

    public void setResearch32_researcher(research32_Researcher research32_researcher) {
        this.research32_researcher = research32_researcher;
    }
    public research32_Paragraph getResearch32_paragraph() {
        return research32_paragraph;
    }

    public void setResearch32_paragraph(research32_Paragraph research32_paragraph) {
        this.research32_paragraph = research32_paragraph;
    }

}