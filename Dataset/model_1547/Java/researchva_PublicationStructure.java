





import java.util.List;
import java.util.ArrayList;

public class researchva_PublicationStructure extends Named {






    private List<researchva_Researcher> researchva_researchers;




    private List<researchva_Paper> researchva_papers;


    public researchva_PublicationStructure(
    ) {
        super(
        );
        this.researchva_researchers = new ArrayList<>();
        this.researchva_papers = new ArrayList<>();
    }

    public researchva_PublicationStructure(
        ArrayList<researchva_Researcher> researchva_researchers,        ArrayList<researchva_Paper> researchva_papers    ) {
        this.researchva_researchers = researchva_researchers;
        this.researchva_papers = researchva_papers;
    }


    public List<researchva_Researcher> getResearchva_researchers() {
        return researchva_researchers;
    }

    public void addResearchva_researcher(Researchva_researcher researchva_researcher) {
        this.researchva_researchers.add(researchva_researcher);
    }
    public List<researchva_Paper> getResearchva_papers() {
        return researchva_papers;
    }

    public void addResearchva_paper(Researchva_paper researchva_paper) {
        this.researchva_papers.add(researchva_paper);
    }

}