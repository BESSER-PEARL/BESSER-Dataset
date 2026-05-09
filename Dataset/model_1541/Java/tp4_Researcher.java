





import java.util.List;
import java.util.ArrayList;

public class tp4_Researcher  {

    private String forName;
    private String name;





    private tp4_Position tp4_position;




    private List<tp4_Paper> tp4_papers;




    private tp4_PublicationStructure tp4_publicationstructure;




    private tp4_Paper tp4_paper;


    public tp4_Researcher(
        String forName,        String name    ) {
        this.forName = forName;
        this.name = name;
        this.tp4_papers = new ArrayList<>();
    }

    public tp4_Researcher(
        String forName,        String name        ArrayList<tp4_Paper> tp4_papers    ) {
        this.forName = forName;
        this.name = name;
        this.tp4_papers = tp4_papers;
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

    public tp4_Position getTp4_position() {
        return tp4_position;
    }

    public void setTp4_position(tp4_Position tp4_position) {
        this.tp4_position = tp4_position;
    }
    public List<tp4_Paper> getTp4_papers() {
        return tp4_papers;
    }

    public void addTp4_paper(Tp4_paper tp4_paper) {
        this.tp4_papers.add(tp4_paper);
    }
    public tp4_PublicationStructure getTp4_publicationstructure() {
        return tp4_publicationstructure;
    }

    public void setTp4_publicationstructure(tp4_PublicationStructure tp4_publicationstructure) {
        this.tp4_publicationstructure = tp4_publicationstructure;
    }
    public tp4_Paper getTp4_paper() {
        return tp4_paper;
    }

    public void setTp4_paper(tp4_Paper tp4_paper) {
        this.tp4_paper = tp4_paper;
    }

}