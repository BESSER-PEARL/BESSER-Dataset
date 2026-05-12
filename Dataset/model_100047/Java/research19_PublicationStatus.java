





import java.util.List;
import java.util.ArrayList;

public class research19_PublicationStatus  {

    private String label;





    private research19_PublicationSystem research19_publicationsystem;




    private List<research19_State> research19_states;


    public research19_PublicationStatus(
        String label    ) {
        this.label = label;
        this.research19_states = new ArrayList<>();
    }

    public research19_PublicationStatus(
        String label        ArrayList<research19_State> research19_states    ) {
        this.label = label;
        this.research19_states = research19_states;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public research19_PublicationSystem getResearch19_publicationsystem() {
        return research19_publicationsystem;
    }

    public void setResearch19_publicationsystem(research19_PublicationSystem research19_publicationsystem) {
        this.research19_publicationsystem = research19_publicationsystem;
    }
    public List<research19_State> getResearch19_states() {
        return research19_states;
    }

    public void addResearch19_state(Research19_state research19_state) {
        this.research19_states.add(research19_state);
    }

}