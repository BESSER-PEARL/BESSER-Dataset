





import java.util.List;
import java.util.ArrayList;

public class research16_Paper extends Named {






    private List<research16_Researcher> research16_researchers;




    private research16_Researcher research16_researcher;




    private research16_Paper research16_paper;


    public research16_Paper(
    ) {
        super(
        );
        this.research16_researchers = new ArrayList<>();
    }

    public research16_Paper(
        ArrayList<research16_Researcher> research16_researchers    ) {
        this.research16_researchers = research16_researchers;
    }


    public List<research16_Researcher> getResearch16_researchers() {
        return research16_researchers;
    }

    public void addResearch16_researcher(Research16_researcher research16_researcher) {
        this.research16_researchers.add(research16_researcher);
    }
    public research16_Researcher getResearch16_researcher() {
        return research16_researcher;
    }

    public void setResearch16_researcher(research16_Researcher research16_researcher) {
        this.research16_researcher = research16_researcher;
    }
    public research16_Paper getResearch16_paper() {
        return research16_paper;
    }

    public void setResearch16_paper(research16_Paper research16_paper) {
        this.research16_paper = research16_paper;
    }

}