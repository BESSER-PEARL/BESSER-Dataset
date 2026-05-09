





import java.util.List;
import java.util.ArrayList;

public class research_Paper extends Named {






    private List<research_Researcher> research_researchers;




    private research_Paper research_paper;




    private research_Researcher research_researcher;


    public research_Paper(
    ) {
        super(
        );
        this.research_researchers = new ArrayList<>();
    }

    public research_Paper(
        ArrayList<research_Researcher> research_researchers    ) {
        this.research_researchers = research_researchers;
    }


    public List<research_Researcher> getResearch_researchers() {
        return research_researchers;
    }

    public void addResearch_researcher(Research_researcher research_researcher) {
        this.research_researchers.add(research_researcher);
    }
    public research_Paper getResearch_paper() {
        return research_paper;
    }

    public void setResearch_paper(research_Paper research_paper) {
        this.research_paper = research_paper;
    }
    public research_Researcher getResearch_researcher() {
        return research_researcher;
    }

    public void setResearch_researcher(research_Researcher research_researcher) {
        this.research_researcher = research_researcher;
    }

}