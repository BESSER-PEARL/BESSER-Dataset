





import java.util.List;
import java.util.ArrayList;

public class research13_Paper extends Named {






    private research13_Researcher research13_researcher;




    private List<research13_Researcher> research13_researchers;




    private research13_Paper research13_paper;


    public research13_Paper(
    ) {
        super(
        );
        this.research13_researchers = new ArrayList<>();
    }

    public research13_Paper(
        ArrayList<research13_Researcher> research13_researchers    ) {
        this.research13_researchers = research13_researchers;
    }


    public research13_Researcher getResearch13_researcher() {
        return research13_researcher;
    }

    public void setResearch13_researcher(research13_Researcher research13_researcher) {
        this.research13_researcher = research13_researcher;
    }
    public List<research13_Researcher> getResearch13_researchers() {
        return research13_researchers;
    }

    public void addResearch13_researcher(Research13_researcher research13_researcher) {
        this.research13_researchers.add(research13_researcher);
    }
    public research13_Paper getResearch13_paper() {
        return research13_paper;
    }

    public void setResearch13_paper(research13_Paper research13_paper) {
        this.research13_paper = research13_paper;
    }

}