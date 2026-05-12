





import java.util.List;
import java.util.ArrayList;

public class tp4_Write extends Labelled {

    private int timeSpent;





    private tp4_Paragraph tp4_paragraph;




    private tp4_Researcher tp4_researcher;


    public tp4_Write(
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

    public tp4_Paragraph getTp4_paragraph() {
        return tp4_paragraph;
    }

    public void setTp4_paragraph(tp4_Paragraph tp4_paragraph) {
        this.tp4_paragraph = tp4_paragraph;
    }
    public tp4_Researcher getTp4_researcher() {
        return tp4_researcher;
    }

    public void setTp4_researcher(tp4_Researcher tp4_researcher) {
        this.tp4_researcher = tp4_researcher;
    }

}