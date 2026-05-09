





import java.util.List;
import java.util.ArrayList;

public class researchva_Paper extends Named {






    private researchva_Paper researchva_paper;




    private researchva_Researcher researchva_researcher;




    private List<researchva_Researcher> researchva_researchers;


    public researchva_Paper(
    ) {
        super(
        );
        this.researchva_researchers = new ArrayList<>();
    }

    public researchva_Paper(
        ArrayList<researchva_Researcher> researchva_researchers    ) {
        this.researchva_researchers = researchva_researchers;
    }


    public researchva_Paper getResearchva_paper() {
        return researchva_paper;
    }

    public void setResearchva_paper(researchva_Paper researchva_paper) {
        this.researchva_paper = researchva_paper;
    }
    public researchva_Researcher getResearchva_researcher() {
        return researchva_researcher;
    }

    public void setResearchva_researcher(researchva_Researcher researchva_researcher) {
        this.researchva_researcher = researchva_researcher;
    }
    public List<researchva_Researcher> getResearchva_researchers() {
        return researchva_researchers;
    }

    public void addResearchva_researcher(Researchva_researcher researchva_researcher) {
        this.researchva_researchers.add(researchva_researcher);
    }

}