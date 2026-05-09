





import java.util.List;
import java.util.ArrayList;

public class research31_PublicationStructure extends Named {






    private research31_PublicationSystem research31_publicationsystem;




    private List<research31_Paper> research31_papers;


    public research31_PublicationStructure(
    ) {
        super(
        );
        this.research31_papers = new ArrayList<>();
    }

    public research31_PublicationStructure(
        ArrayList<research31_Paper> research31_papers    ) {
        this.research31_papers = research31_papers;
    }


    public research31_PublicationSystem getResearch31_publicationsystem() {
        return research31_publicationsystem;
    }

    public void setResearch31_publicationsystem(research31_PublicationSystem research31_publicationsystem) {
        this.research31_publicationsystem = research31_publicationsystem;
    }
    public List<research31_Paper> getResearch31_papers() {
        return research31_papers;
    }

    public void addResearch31_paper(Research31_paper research31_paper) {
        this.research31_papers.add(research31_paper);
    }

}