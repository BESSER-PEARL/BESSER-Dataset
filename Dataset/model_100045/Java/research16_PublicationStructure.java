





import java.util.List;
import java.util.ArrayList;

public class research16_PublicationStructure extends Named {






    private List<research16_Paper> research16_papers;




    private List<research16_Researcher> research16_researchers;


    public research16_PublicationStructure(
    ) {
        super(
        );
        this.research16_papers = new ArrayList<>();
        this.research16_researchers = new ArrayList<>();
    }

    public research16_PublicationStructure(
        ArrayList<research16_Paper> research16_papers,        ArrayList<research16_Researcher> research16_researchers    ) {
        this.research16_papers = research16_papers;
        this.research16_researchers = research16_researchers;
    }


    public List<research16_Paper> getResearch16_papers() {
        return research16_papers;
    }

    public void addResearch16_paper(Research16_paper research16_paper) {
        this.research16_papers.add(research16_paper);
    }
    public List<research16_Researcher> getResearch16_researchers() {
        return research16_researchers;
    }

    public void addResearch16_researcher(Research16_researcher research16_researcher) {
        this.research16_researchers.add(research16_researcher);
    }

}