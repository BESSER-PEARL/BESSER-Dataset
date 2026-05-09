





import java.util.List;
import java.util.ArrayList;

public class tp6_Researcher  {

    private String name;
    private String forName;





    private tp6_Position tp6_position;




    private List<tp6_Collaboration> tp6_collaborations;


    public tp6_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
        this.tp6_collaborations = new ArrayList<>();
    }

    public tp6_Researcher(
        String name,        String forName        ArrayList<tp6_Collaboration> tp6_collaborations    ) {
        this.name = name;
        this.forName = forName;
        this.tp6_collaborations = tp6_collaborations;
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

    public tp6_Position getTp6_position() {
        return tp6_position;
    }

    public void setTp6_position(tp6_Position tp6_position) {
        this.tp6_position = tp6_position;
    }
    public List<tp6_Collaboration> getTp6_collaborations() {
        return tp6_collaborations;
    }

    public void addTp6_collaboration(Tp6_collaboration tp6_collaboration) {
        this.tp6_collaborations.add(tp6_collaboration);
    }

}