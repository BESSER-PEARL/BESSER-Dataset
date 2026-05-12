





import java.util.List;
import java.util.ArrayList;

public class research13_PublicationStructure extends Named {






    private List<research13_Paper> research13_papers;




    private List<research13_Researcher> research13_researchers;


    public research13_PublicationStructure(
    ) {
        super(
        );
        this.research13_papers = new ArrayList<>();
        this.research13_researchers = new ArrayList<>();
    }

    public research13_PublicationStructure(
        ArrayList<research13_Paper> research13_papers,        ArrayList<research13_Researcher> research13_researchers    ) {
        this.research13_papers = research13_papers;
        this.research13_researchers = research13_researchers;
    }


    public List<research13_Paper> getResearch13_papers() {
        return research13_papers;
    }

    public void addResearch13_paper(Research13_paper research13_paper) {
        this.research13_papers.add(research13_paper);
    }
    public List<research13_Researcher> getResearch13_researchers() {
        return research13_researchers;
    }

    public void addResearch13_researcher(Research13_researcher research13_researcher) {
        this.research13_researchers.add(research13_researcher);
    }

}