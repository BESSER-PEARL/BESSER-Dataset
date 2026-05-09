





import java.util.List;
import java.util.ArrayList;

public class research16_PublicationStructure extends Named {






    private research16_PublicationSystem research16_publicationsystem;




    private List<research16_Paper> research16_papers;


    public research16_PublicationStructure(
    ) {
        super(
        );
        this.research16_papers = new ArrayList<>();
    }

    public research16_PublicationStructure(
        ArrayList<research16_Paper> research16_papers    ) {
        this.research16_papers = research16_papers;
    }


    public research16_PublicationSystem getResearch16_publicationsystem() {
        return research16_publicationsystem;
    }

    public void setResearch16_publicationsystem(research16_PublicationSystem research16_publicationsystem) {
        this.research16_publicationsystem = research16_publicationsystem;
    }
    public List<research16_Paper> getResearch16_papers() {
        return research16_papers;
    }

    public void addResearch16_paper(Research16_paper research16_paper) {
        this.research16_papers.add(research16_paper);
    }

}