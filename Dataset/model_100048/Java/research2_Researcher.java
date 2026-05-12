





import java.util.List;
import java.util.ArrayList;

public class research2_Researcher  {

    private String forName;
    private String name;





    private List<research2_Paper> research2_papers;




    private research2_Position research2_position;




    private research2_Paper research2_paper;




    private research2_PublicationStructure research2_publicationstructure;


    public research2_Researcher(
        String forName,        String name    ) {
        this.forName = forName;
        this.name = name;
        this.research2_papers = new ArrayList<>();
    }

    public research2_Researcher(
        String forName,        String name        ArrayList<research2_Paper> research2_papers    ) {
        this.forName = forName;
        this.name = name;
        this.research2_papers = research2_papers;
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

    public List<research2_Paper> getResearch2_papers() {
        return research2_papers;
    }

    public void addResearch2_paper(Research2_paper research2_paper) {
        this.research2_papers.add(research2_paper);
    }
    public research2_Position getResearch2_position() {
        return research2_position;
    }

    public void setResearch2_position(research2_Position research2_position) {
        this.research2_position = research2_position;
    }
    public research2_Paper getResearch2_paper() {
        return research2_paper;
    }

    public void setResearch2_paper(research2_Paper research2_paper) {
        this.research2_paper = research2_paper;
    }
    public research2_PublicationStructure getResearch2_publicationstructure() {
        return research2_publicationstructure;
    }

    public void setResearch2_publicationstructure(research2_PublicationStructure research2_publicationstructure) {
        this.research2_publicationstructure = research2_publicationstructure;
    }

}