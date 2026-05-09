





import java.util.List;
import java.util.ArrayList;

public class research15_PublicationStructure extends Named {






    private List<research15_Paper> research15_papers;




    private research15_PublicationSystem research15_publicationsystem;


    public research15_PublicationStructure(
    ) {
        super(
        );
        this.research15_papers = new ArrayList<>();
    }

    public research15_PublicationStructure(
        ArrayList<research15_Paper> research15_papers    ) {
        this.research15_papers = research15_papers;
    }


    public List<research15_Paper> getResearch15_papers() {
        return research15_papers;
    }

    public void addResearch15_paper(Research15_paper research15_paper) {
        this.research15_papers.add(research15_paper);
    }
    public research15_PublicationSystem getResearch15_publicationsystem() {
        return research15_publicationsystem;
    }

    public void setResearch15_publicationsystem(research15_PublicationSystem research15_publicationsystem) {
        this.research15_publicationsystem = research15_publicationsystem;
    }

}