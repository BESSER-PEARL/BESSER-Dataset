





import java.util.List;
import java.util.ArrayList;

public class research31_Researcher  {

    private String name;
    private String forName;





    private List<research31_Paper> research31_papers;




    private research31_Position research31_position;




    private research31_PublicationStructure research31_publicationstructure;




    private research31_Paper research31_paper;


    public research31_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.research31_papers = new ArrayList<>();
    }

    public research31_Researcher(
        String name,        String forName        ArrayList<research31_Paper> research31_papers    ) {
        this.name = name;
        this.forName = forName;
        this.research31_papers = research31_papers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getForname() {
        return forName;
    }

    public void setForname(String forName) {
        this.forName = forName;
    }

    public List<research31_Paper> getResearch31_papers() {
        return research31_papers;
    }

    public void addResearch31_paper(Research31_paper research31_paper) {
        this.research31_papers.add(research31_paper);
    }
    public research31_Position getResearch31_position() {
        return research31_position;
    }

    public void setResearch31_position(research31_Position research31_position) {
        this.research31_position = research31_position;
    }
    public research31_PublicationStructure getResearch31_publicationstructure() {
        return research31_publicationstructure;
    }

    public void setResearch31_publicationstructure(research31_PublicationStructure research31_publicationstructure) {
        this.research31_publicationstructure = research31_publicationstructure;
    }
    public research31_Paper getResearch31_paper() {
        return research31_paper;
    }

    public void setResearch31_paper(research31_Paper research31_paper) {
        this.research31_paper = research31_paper;
    }

}