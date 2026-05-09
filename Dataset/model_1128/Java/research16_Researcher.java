





import java.util.List;
import java.util.ArrayList;

public class research16_Researcher  {

    private String forName;
    private String name;





    private List<research16_Paper> research16_papers;




    private research16_Position research16_position;




    private research16_Paper research16_paper;




    private research16_PublicationStructure research16_publicationstructure;


    public research16_Researcher(
        String forName,        String name    ) {
        this.forName = forName;
        this.name = name;
        this.research16_papers = new ArrayList<>();
    }

    public research16_Researcher(
        String forName,        String name        ArrayList<research16_Paper> research16_papers    ) {
        this.forName = forName;
        this.name = name;
        this.research16_papers = research16_papers;
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

    public List<research16_Paper> getResearch16_papers() {
        return research16_papers;
    }

    public void addResearch16_paper(Research16_paper research16_paper) {
        this.research16_papers.add(research16_paper);
    }
    public research16_Position getResearch16_position() {
        return research16_position;
    }

    public void setResearch16_position(research16_Position research16_position) {
        this.research16_position = research16_position;
    }
    public research16_Paper getResearch16_paper() {
        return research16_paper;
    }

    public void setResearch16_paper(research16_Paper research16_paper) {
        this.research16_paper = research16_paper;
    }
    public research16_PublicationStructure getResearch16_publicationstructure() {
        return research16_publicationstructure;
    }

    public void setResearch16_publicationstructure(research16_PublicationStructure research16_publicationstructure) {
        this.research16_publicationstructure = research16_publicationstructure;
    }

}