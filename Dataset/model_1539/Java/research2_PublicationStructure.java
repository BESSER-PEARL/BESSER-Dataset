





import java.util.List;
import java.util.ArrayList;

public class research2_PublicationStructure extends Named {






    private List<research2_Paper> research2_papers;




    private List<research2_Researcher> research2_researchers;




    private research2_PublicationSystem research2_publicationsystem;


    public research2_PublicationStructure(
    ) {
        super(
        );
        this.research2_papers = new ArrayList<>();
        this.research2_researchers = new ArrayList<>();
    }

    public research2_PublicationStructure(
        ArrayList<research2_Paper> research2_papers,        ArrayList<research2_Researcher> research2_researchers    ) {
        this.research2_papers = research2_papers;
        this.research2_researchers = research2_researchers;
    }


    public List<research2_Paper> getResearch2_papers() {
        return research2_papers;
    }

    public void addResearch2_paper(Research2_paper research2_paper) {
        this.research2_papers.add(research2_paper);
    }
    public List<research2_Researcher> getResearch2_researchers() {
        return research2_researchers;
    }

    public void addResearch2_researcher(Research2_researcher research2_researcher) {
        this.research2_researchers.add(research2_researcher);
    }
    public research2_PublicationSystem getResearch2_publicationsystem() {
        return research2_publicationsystem;
    }

    public void setResearch2_publicationsystem(research2_PublicationSystem research2_publicationsystem) {
        this.research2_publicationsystem = research2_publicationsystem;
    }

}