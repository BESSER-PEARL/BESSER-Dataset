





import java.util.List;
import java.util.ArrayList;

public class research19_Researcher  {

    private String forName;
    private String name;





    private List<research19_Paper> research19_papers;




    private research19_Paper research19_paper;




    private research19_Position research19_position;




    private research19_PublicationStructure research19_publicationstructure;


    public research19_Researcher(
        String forName,        String name    ) {
        this.forName = forName;
        this.name = name;
        this.research19_papers = new ArrayList<>();
    }

    public research19_Researcher(
        String forName,        String name        ArrayList<research19_Paper> research19_papers    ) {
        this.forName = forName;
        this.name = name;
        this.research19_papers = research19_papers;
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

    public List<research19_Paper> getResearch19_papers() {
        return research19_papers;
    }

    public void addResearch19_paper(Research19_paper research19_paper) {
        this.research19_papers.add(research19_paper);
    }
    public research19_Paper getResearch19_paper() {
        return research19_paper;
    }

    public void setResearch19_paper(research19_Paper research19_paper) {
        this.research19_paper = research19_paper;
    }
    public research19_Position getResearch19_position() {
        return research19_position;
    }

    public void setResearch19_position(research19_Position research19_position) {
        this.research19_position = research19_position;
    }
    public research19_PublicationStructure getResearch19_publicationstructure() {
        return research19_publicationstructure;
    }

    public void setResearch19_publicationstructure(research19_PublicationStructure research19_publicationstructure) {
        this.research19_publicationstructure = research19_publicationstructure;
    }

}