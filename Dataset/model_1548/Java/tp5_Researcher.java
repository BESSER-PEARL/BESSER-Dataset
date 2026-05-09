





import java.util.List;
import java.util.ArrayList;

public class tp5_Researcher  {

    private String forName;
    private String name;





    private tp5_PublicationStructure tp5_publicationstructure;




    private List<tp5_Collaboration> tp5_collaborations;


    public tp5_Researcher(
        String forName,        String name    ) {
        this.forName = forName;
        this.name = name;
        this.tp5_collaborations = new ArrayList<>();
    }

    public tp5_Researcher(
        String forName,        String name        ArrayList<tp5_Collaboration> tp5_collaborations    ) {
        this.forName = forName;
        this.name = name;
        this.tp5_collaborations = tp5_collaborations;
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

    public tp5_PublicationStructure getTp5_publicationstructure() {
        return tp5_publicationstructure;
    }

    public void setTp5_publicationstructure(tp5_PublicationStructure tp5_publicationstructure) {
        this.tp5_publicationstructure = tp5_publicationstructure;
    }
    public List<tp5_Collaboration> getTp5_collaborations() {
        return tp5_collaborations;
    }

    public void addTp5_collaboration(Tp5_collaboration tp5_collaboration) {
        this.tp5_collaborations.add(tp5_collaboration);
    }

}