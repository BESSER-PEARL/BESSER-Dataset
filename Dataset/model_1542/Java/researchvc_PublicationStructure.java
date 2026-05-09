





import java.util.List;
import java.util.ArrayList;

public class researchvc_PublicationStructure extends Named {






    private List<researchvc_Keyword> researchvc_keywords;




    private List<researchvc_Paper> researchvc_papers;




    private List<researchvc_Researcher> researchvc_researchers;


    public researchvc_PublicationStructure(
    ) {
        super(
        );
        this.researchvc_keywords = new ArrayList<>();
        this.researchvc_papers = new ArrayList<>();
        this.researchvc_researchers = new ArrayList<>();
    }

    public researchvc_PublicationStructure(
        ArrayList<researchvc_Keyword> researchvc_keywords,        ArrayList<researchvc_Paper> researchvc_papers,        ArrayList<researchvc_Researcher> researchvc_researchers    ) {
        this.researchvc_keywords = researchvc_keywords;
        this.researchvc_papers = researchvc_papers;
        this.researchvc_researchers = researchvc_researchers;
    }


    public List<researchvc_Keyword> getResearchvc_keywords() {
        return researchvc_keywords;
    }

    public void addResearchvc_keyword(Researchvc_keyword researchvc_keyword) {
        this.researchvc_keywords.add(researchvc_keyword);
    }
    public List<researchvc_Paper> getResearchvc_papers() {
        return researchvc_papers;
    }

    public void addResearchvc_paper(Researchvc_paper researchvc_paper) {
        this.researchvc_papers.add(researchvc_paper);
    }
    public List<researchvc_Researcher> getResearchvc_researchers() {
        return researchvc_researchers;
    }

    public void addResearchvc_researcher(Researchvc_researcher researchvc_researcher) {
        this.researchvc_researchers.add(researchvc_researcher);
    }

}