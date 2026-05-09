





import java.util.List;
import java.util.ArrayList;

public class research2_Paper extends Named {






    private research2_Paper research2_paper;




    private research2_Researcher research2_researcher;




    private List<research2_Researcher> research2_researchers;


    public research2_Paper(
    ) {
        super(
        );
        this.research2_researchers = new ArrayList<>();
    }

    public research2_Paper(
        ArrayList<research2_Researcher> research2_researchers    ) {
        this.research2_researchers = research2_researchers;
    }


    public research2_Paper getResearch2_paper() {
        return research2_paper;
    }

    public void setResearch2_paper(research2_Paper research2_paper) {
        this.research2_paper = research2_paper;
    }
    public research2_Researcher getResearch2_researcher() {
        return research2_researcher;
    }

    public void setResearch2_researcher(research2_Researcher research2_researcher) {
        this.research2_researcher = research2_researcher;
    }
    public List<research2_Researcher> getResearch2_researchers() {
        return research2_researchers;
    }

    public void addResearch2_researcher(Research2_researcher research2_researcher) {
        this.research2_researchers.add(research2_researcher);
    }

}