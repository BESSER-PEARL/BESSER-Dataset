





import java.util.List;
import java.util.ArrayList;

public class research32_Researcher  {

    private String name;
    private String forName;





    private List<research32_Collaboration> research32_collaborations;




    private research32_Paper research32_paper;




    private research32_Position research32_position;




    private List<research32_Paper> research32_papers;




    private research32_PublicationStructure research32_publicationstructure;


    public research32_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.research32_collaborations = new ArrayList<>();
        this.research32_papers = new ArrayList<>();
    }

    public research32_Researcher(
        String name,        String forName        ArrayList<research32_Collaboration> research32_collaborations,        ArrayList<research32_Paper> research32_papers    ) {
        this.name = name;
        this.forName = forName;
        this.research32_collaborations = research32_collaborations;
        this.research32_papers = research32_papers;
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

    public List<research32_Collaboration> getResearch32_collaborations() {
        return research32_collaborations;
    }

    public void addResearch32_collaboration(Research32_collaboration research32_collaboration) {
        this.research32_collaborations.add(research32_collaboration);
    }
    public research32_Paper getResearch32_paper() {
        return research32_paper;
    }

    public void setResearch32_paper(research32_Paper research32_paper) {
        this.research32_paper = research32_paper;
    }
    public research32_Position getResearch32_position() {
        return research32_position;
    }

    public void setResearch32_position(research32_Position research32_position) {
        this.research32_position = research32_position;
    }
    public List<research32_Paper> getResearch32_papers() {
        return research32_papers;
    }

    public void addResearch32_paper(Research32_paper research32_paper) {
        this.research32_papers.add(research32_paper);
    }
    public research32_PublicationStructure getResearch32_publicationstructure() {
        return research32_publicationstructure;
    }

    public void setResearch32_publicationstructure(research32_PublicationStructure research32_publicationstructure) {
        this.research32_publicationstructure = research32_publicationstructure;
    }

}