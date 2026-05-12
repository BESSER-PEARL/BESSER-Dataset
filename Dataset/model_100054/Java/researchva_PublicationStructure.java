





import java.util.List;
import java.util.ArrayList;

public class researchva_PublicationStructure extends Named {






    private List<researchva_Researcher> researchva_researchers;




    private List<researchva_Paper> researchva_papers;




    private List<researchva_Keyword> researchva_keywords;


    public researchva_PublicationStructure(
    ) {
        super(
        );
        this.researchva_researchers = new ArrayList<>();
        this.researchva_papers = new ArrayList<>();
        this.researchva_keywords = new ArrayList<>();
    }

    public researchva_PublicationStructure(
        ArrayList<researchva_Researcher> researchva_researchers,        ArrayList<researchva_Paper> researchva_papers,        ArrayList<researchva_Keyword> researchva_keywords    ) {
        this.researchva_researchers = researchva_researchers;
        this.researchva_papers = researchva_papers;
        this.researchva_keywords = researchva_keywords;
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
    public List<researchva_Keyword> getResearchva_keywords() {
        return researchva_keywords;
    }

    public void addResearchva_keyword(Researchva_keyword researchva_keyword) {
        this.researchva_keywords.add(researchva_keyword);
    }

}