





import java.util.List;
import java.util.ArrayList;

public class research13_Researcher  {

    private String forName;
    private String name;





    private research13_PublicationStructure research13_publicationstructure;




    private research13_Position research13_position;




    private research13_Paper research13_paper;




    private List<research13_Paper> research13_papers;


    public research13_Researcher(
        String forName,        String name    ) {
        this.forName = forName;
        this.name = name;
        this.research13_papers = new ArrayList<>();
    }

    public research13_Researcher(
        String forName,        String name        ArrayList<research13_Paper> research13_papers    ) {
        this.forName = forName;
        this.name = name;
        this.research13_papers = research13_papers;
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

    public research13_PublicationStructure getResearch13_publicationstructure() {
        return research13_publicationstructure;
    }

    public void setResearch13_publicationstructure(research13_PublicationStructure research13_publicationstructure) {
        this.research13_publicationstructure = research13_publicationstructure;
    }
    public research13_Position getResearch13_position() {
        return research13_position;
    }

    public void setResearch13_position(research13_Position research13_position) {
        this.research13_position = research13_position;
    }
    public research13_Paper getResearch13_paper() {
        return research13_paper;
    }

    public void setResearch13_paper(research13_Paper research13_paper) {
        this.research13_paper = research13_paper;
    }
    public List<research13_Paper> getResearch13_papers() {
        return research13_papers;
    }

    public void addResearch13_paper(Research13_paper research13_paper) {
        this.research13_papers.add(research13_paper);
    }

}