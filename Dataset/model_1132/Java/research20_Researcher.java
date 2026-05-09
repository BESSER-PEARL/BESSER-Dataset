





import java.util.List;
import java.util.ArrayList;

public class research20_Researcher  {

    private String forName;
    private String name;





    private research20_Position research20_position;




    private research20_Paper research20_paper;




    private List<research20_Paper> research20_papers;




    private research20_PublicationStructure research20_publicationstructure;


    public research20_Researcher(
        String forName,        String name    ) {
        this.forName = forName;
        this.name = name;
        this.research20_papers = new ArrayList<>();
    }

    public research20_Researcher(
        String forName,        String name        ArrayList<research20_Paper> research20_papers    ) {
        this.forName = forName;
        this.name = name;
        this.research20_papers = research20_papers;
    }

    public String getForname() {
        return forName;
    }

    public void setForname(String forName) {
        this.forName = forName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public research20_Position getResearch20_position() {
        return research20_position;
    }

    public void setResearch20_position(research20_Position research20_position) {
        this.research20_position = research20_position;
    }
    public research20_Paper getResearch20_paper() {
        return research20_paper;
    }

    public void setResearch20_paper(research20_Paper research20_paper) {
        this.research20_paper = research20_paper;
    }
    public List<research20_Paper> getResearch20_papers() {
        return research20_papers;
    }

    public void addResearch20_paper(Research20_paper research20_paper) {
        this.research20_papers.add(research20_paper);
    }
    public research20_PublicationStructure getResearch20_publicationstructure() {
        return research20_publicationstructure;
    }

    public void setResearch20_publicationstructure(research20_PublicationStructure research20_publicationstructure) {
        this.research20_publicationstructure = research20_publicationstructure;
    }

}