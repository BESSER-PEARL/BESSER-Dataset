





import java.util.List;
import java.util.ArrayList;

public class research15_Researcher  {

    private String name;
    private String forName;





    private research15_Paper research15_paper;




    private research15_PublicationStructure research15_publicationstructure;




    private List<research15_Paper> research15_papers;




    private research15_Position research15_position;


    public research15_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.research15_papers = new ArrayList<>();
    }

    public research15_Researcher(
        String name,        String forName        ArrayList<research15_Paper> research15_papers    ) {
        this.name = name;
        this.forName = forName;
        this.research15_papers = research15_papers;
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

    public research15_Paper getResearch15_paper() {
        return research15_paper;
    }

    public void setResearch15_paper(research15_Paper research15_paper) {
        this.research15_paper = research15_paper;
    }
    public research15_PublicationStructure getResearch15_publicationstructure() {
        return research15_publicationstructure;
    }

    public void setResearch15_publicationstructure(research15_PublicationStructure research15_publicationstructure) {
        this.research15_publicationstructure = research15_publicationstructure;
    }
    public List<research15_Paper> getResearch15_papers() {
        return research15_papers;
    }

    public void addResearch15_paper(Research15_paper research15_paper) {
        this.research15_papers.add(research15_paper);
    }
    public research15_Position getResearch15_position() {
        return research15_position;
    }

    public void setResearch15_position(research15_Position research15_position) {
        this.research15_position = research15_position;
    }

}