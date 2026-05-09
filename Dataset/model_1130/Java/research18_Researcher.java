





import java.util.List;
import java.util.ArrayList;

public class research18_Researcher  {

    private String name;
    private String forName;





    private research18_PublicationStructure research18_publicationstructure;




    private research18_Paper research18_paper;




    private List<research18_Paper> research18_papers;




    private research18_Position research18_position;


    public research18_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.research18_papers = new ArrayList<>();
    }

    public research18_Researcher(
        String name,        String forName        ArrayList<research18_Paper> research18_papers    ) {
        this.name = name;
        this.forName = forName;
        this.research18_papers = research18_papers;
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

    public research18_PublicationStructure getResearch18_publicationstructure() {
        return research18_publicationstructure;
    }

    public void setResearch18_publicationstructure(research18_PublicationStructure research18_publicationstructure) {
        this.research18_publicationstructure = research18_publicationstructure;
    }
    public research18_Paper getResearch18_paper() {
        return research18_paper;
    }

    public void setResearch18_paper(research18_Paper research18_paper) {
        this.research18_paper = research18_paper;
    }
    public List<research18_Paper> getResearch18_papers() {
        return research18_papers;
    }

    public void addResearch18_paper(Research18_paper research18_paper) {
        this.research18_papers.add(research18_paper);
    }
    public research18_Position getResearch18_position() {
        return research18_position;
    }

    public void setResearch18_position(research18_Position research18_position) {
        this.research18_position = research18_position;
    }

}