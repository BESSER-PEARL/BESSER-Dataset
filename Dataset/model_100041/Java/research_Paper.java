





import java.util.List;
import java.util.ArrayList;

public class research_Paper extends Named {






    private research_Paper research_paper;




    private research_Keyword research_keyword;




    private research_PublicationStructure research_publicationstructure;




    private List<research_Researcher> research_researchers;




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


    public research_Paper getResearch_paper() {
        return research_paper;
    }

    public void setResearch_paper(research_Paper research_paper) {
        this.research_paper = research_paper;
    }
    public research_Keyword getResearch_keyword() {
        return research_keyword;
    }

    public void setResearch_keyword(research_Keyword research_keyword) {
        this.research_keyword = research_keyword;
    }
    public research_PublicationStructure getResearch_publicationstructure() {
        return research_publicationstructure;
    }

    public void setResearch_publicationstructure(research_PublicationStructure research_publicationstructure) {
        this.research_publicationstructure = research_publicationstructure;
    }
    public List<research_Researcher> getResearch_researchers() {
        return research_researchers;
    }

    public void addResearch_researcher(Research_researcher research_researcher) {
        this.research_researchers.add(research_researcher);
    }
    public research_Researcher getResearch_researcher() {
        return research_researcher;
    }

    public void setResearch_researcher(research_Researcher research_researcher) {
        this.research_researcher = research_researcher;
    }

}