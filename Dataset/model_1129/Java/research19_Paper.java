





import java.util.List;
import java.util.ArrayList;

public class research19_Paper extends Named {






    private List<research19_Researcher> research19_researchers;




    private research19_Paper research19_paper;




    private research19_Researcher research19_researcher;


    public research19_Paper(
    ) {
        super(
        );
        this.research19_researchers = new ArrayList<>();
    }

    public research19_Paper(
        ArrayList<research19_Researcher> research19_researchers    ) {
        this.research19_researchers = research19_researchers;
    }


    public List<research19_Researcher> getResearch19_researchers() {
        return research19_researchers;
    }

    public void addResearch19_researcher(Research19_researcher research19_researcher) {
        this.research19_researchers.add(research19_researcher);
    }
    public research19_Paper getResearch19_paper() {
        return research19_paper;
    }

    public void setResearch19_paper(research19_Paper research19_paper) {
        this.research19_paper = research19_paper;
    }
    public research19_Researcher getResearch19_researcher() {
        return research19_researcher;
    }

    public void setResearch19_researcher(research19_Researcher research19_researcher) {
        this.research19_researcher = research19_researcher;
    }

}