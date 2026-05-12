





import java.util.List;
import java.util.ArrayList;

public class research101_Researcher  {

    private String name;
    private String forName;





    private List<research101_Paper> research101_papers;




    private research101_PublicationStructure research101_publicationstructure;




    private research101_Position research101_position;




    private research101_Paper research101_paper;


    public research101_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.research101_papers = new ArrayList<>();
    }

    public research101_Researcher(
        String name,        String forName        ArrayList<research101_Paper> research101_papers    ) {
        this.name = name;
        this.forName = forName;
        this.research101_papers = research101_papers;
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

    public List<research101_Paper> getResearch101_papers() {
        return research101_papers;
    }

    public void addResearch101_paper(Research101_paper research101_paper) {
        this.research101_papers.add(research101_paper);
    }
    public research101_PublicationStructure getResearch101_publicationstructure() {
        return research101_publicationstructure;
    }

    public void setResearch101_publicationstructure(research101_PublicationStructure research101_publicationstructure) {
        this.research101_publicationstructure = research101_publicationstructure;
    }
    public research101_Position getResearch101_position() {
        return research101_position;
    }

    public void setResearch101_position(research101_Position research101_position) {
        this.research101_position = research101_position;
    }
    public research101_Paper getResearch101_paper() {
        return research101_paper;
    }

    public void setResearch101_paper(research101_Paper research101_paper) {
        this.research101_paper = research101_paper;
    }

}