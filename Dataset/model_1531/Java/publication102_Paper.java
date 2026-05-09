





import java.util.List;
import java.util.ArrayList;

public class publication102_Paper extends Named {






    private publication102_Researcher publication102_researcher;




    private publication102_Paper publication102_paper;




    private List<publication102_Researcher> publication102_researchers;


    public publication102_Paper(
    ) {
        super(
        );
        this.publication102_researchers = new ArrayList<>();
    }

    public publication102_Paper(
        ArrayList<publication102_Researcher> publication102_researchers    ) {
        this.publication102_researchers = publication102_researchers;
    }


    public publication102_Researcher getPublication102_researcher() {
        return publication102_researcher;
    }

    public void setPublication102_researcher(publication102_Researcher publication102_researcher) {
        this.publication102_researcher = publication102_researcher;
    }
    public publication102_Paper getPublication102_paper() {
        return publication102_paper;
    }

    public void setPublication102_paper(publication102_Paper publication102_paper) {
        this.publication102_paper = publication102_paper;
    }
    public List<publication102_Researcher> getPublication102_researchers() {
        return publication102_researchers;
    }

    public void addPublication102_researcher(Publication102_researcher publication102_researcher) {
        this.publication102_researchers.add(publication102_researcher);
    }

}