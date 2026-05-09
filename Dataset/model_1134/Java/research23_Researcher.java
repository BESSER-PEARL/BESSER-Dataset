





import java.util.List;
import java.util.ArrayList;

public class research23_Researcher  {

    private String name;
    private String forName;





    private research23_PublicationStructure research23_publicationstructure;




    private research23_Position research23_position;




    private List<research23_Paper> research23_papers;




    private research23_Paper research23_paper;


    public research23_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.research23_papers = new ArrayList<>();
    }

    public research23_Researcher(
        String name,        String forName        ArrayList<research23_Paper> research23_papers    ) {
        this.name = name;
        this.forName = forName;
        this.research23_papers = research23_papers;
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

    public research23_PublicationStructure getResearch23_publicationstructure() {
        return research23_publicationstructure;
    }

    public void setResearch23_publicationstructure(research23_PublicationStructure research23_publicationstructure) {
        this.research23_publicationstructure = research23_publicationstructure;
    }
    public research23_Position getResearch23_position() {
        return research23_position;
    }

    public void setResearch23_position(research23_Position research23_position) {
        this.research23_position = research23_position;
    }
    public List<research23_Paper> getResearch23_papers() {
        return research23_papers;
    }

    public void addResearch23_paper(Research23_paper research23_paper) {
        this.research23_papers.add(research23_paper);
    }
    public research23_Paper getResearch23_paper() {
        return research23_paper;
    }

    public void setResearch23_paper(research23_Paper research23_paper) {
        this.research23_paper = research23_paper;
    }

}