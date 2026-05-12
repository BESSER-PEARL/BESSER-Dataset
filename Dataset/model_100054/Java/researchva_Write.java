





import java.util.List;
import java.util.ArrayList;

public class researchva_Write extends Labelled {

    private int timeSpent;





    private researchva_Researcher researchva_researcher;




    private researchva_Paragraph researchva_paragraph;


    public researchva_Write(
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

    public researchva_Researcher getResearchva_researcher() {
        return researchva_researcher;
    }

    public void setResearchva_researcher(researchva_Researcher researchva_researcher) {
        this.researchva_researcher = researchva_researcher;
    }
    public researchva_Paragraph getResearchva_paragraph() {
        return researchva_paragraph;
    }

    public void setResearchva_paragraph(researchva_Paragraph researchva_paragraph) {
        this.researchva_paragraph = researchva_paragraph;
    }

}