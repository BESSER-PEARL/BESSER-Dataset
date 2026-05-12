





import java.util.List;
import java.util.ArrayList;

public class researchvc_Paper extends Named {






    private researchvc_Researcher researchvc_researcher;




    private List<researchvc_Researcher> researchvc_researchers;




    private researchvc_Paper researchvc_paper;


    public researchvc_Paper(
    ) {
        super(
        );
        this.researchvc_researchers = new ArrayList<>();
    }

    public researchvc_Paper(
        ArrayList<researchvc_Researcher> researchvc_researchers    ) {
        this.researchvc_researchers = researchvc_researchers;
    }


    public researchvc_Researcher getResearchvc_researcher() {
        return researchvc_researcher;
    }

    public void setResearchvc_researcher(researchvc_Researcher researchvc_researcher) {
        this.researchvc_researcher = researchvc_researcher;
    }
    public List<researchvc_Researcher> getResearchvc_researchers() {
        return researchvc_researchers;
    }

    public void addResearchvc_researcher(Researchvc_researcher researchvc_researcher) {
        this.researchvc_researchers.add(researchvc_researcher);
    }
    public researchvc_Paper getResearchvc_paper() {
        return researchvc_paper;
    }

    public void setResearchvc_paper(researchvc_Paper researchvc_paper) {
        this.researchvc_paper = researchvc_paper;
    }

}