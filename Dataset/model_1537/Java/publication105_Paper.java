





import java.util.List;
import java.util.ArrayList;

public class publication105_Paper extends Named {






    private publication105_Researcher publication105_researcher;




    private List<publication105_Researcher> publication105_researchers;




    private publication105_Paper publication105_paper;


    public publication105_Paper(
    ) {
        super(
        );
        this.publication105_researchers = new ArrayList<>();
    }

    public publication105_Paper(
        ArrayList<publication105_Researcher> publication105_researchers    ) {
        this.publication105_researchers = publication105_researchers;
    }


    public publication105_Researcher getPublication105_researcher() {
        return publication105_researcher;
    }

    public void setPublication105_researcher(publication105_Researcher publication105_researcher) {
        this.publication105_researcher = publication105_researcher;
    }
    public List<publication105_Researcher> getPublication105_researchers() {
        return publication105_researchers;
    }

    public void addPublication105_researcher(Publication105_researcher publication105_researcher) {
        this.publication105_researchers.add(publication105_researcher);
    }
    public publication105_Paper getPublication105_paper() {
        return publication105_paper;
    }

    public void setPublication105_paper(publication105_Paper publication105_paper) {
        this.publication105_paper = publication105_paper;
    }

}