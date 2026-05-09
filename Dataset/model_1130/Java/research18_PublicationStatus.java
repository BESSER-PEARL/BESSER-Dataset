





import java.util.List;
import java.util.ArrayList;

public class research18_PublicationStatus  {

    private String label;





    private research18_PublicationSystem research18_publicationsystem;




    private List<research18_State> research18_states;


    public research18_PublicationStatus(
        String label    ) {
        this.label = label;
        this.research18_states = new ArrayList<>();
    }

    public research18_PublicationStatus(
        String label        ArrayList<research18_State> research18_states    ) {
        this.label = label;
        this.research18_states = research18_states;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public research18_PublicationSystem getResearch18_publicationsystem() {
        return research18_publicationsystem;
    }

    public void setResearch18_publicationsystem(research18_PublicationSystem research18_publicationsystem) {
        this.research18_publicationsystem = research18_publicationsystem;
    }
    public List<research18_State> getResearch18_states() {
        return research18_states;
    }

    public void addResearch18_state(Research18_state research18_state) {
        this.research18_states.add(research18_state);
    }

}