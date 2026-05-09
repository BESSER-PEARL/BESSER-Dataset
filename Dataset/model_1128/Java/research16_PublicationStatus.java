





import java.util.List;
import java.util.ArrayList;

public class research16_PublicationStatus  {

    private String label;





    private List<research16_State> research16_states;




    private research16_PublicationSystem research16_publicationsystem;


    public research16_PublicationStatus(
        String label    ) {
        this.label = label;
        this.research16_states = new ArrayList<>();
    }

    public research16_PublicationStatus(
        String label        ArrayList<research16_State> research16_states    ) {
        this.label = label;
        this.research16_states = research16_states;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<research16_State> getResearch16_states() {
        return research16_states;
    }

    public void addResearch16_state(Research16_state research16_state) {
        this.research16_states.add(research16_state);
    }
    public research16_PublicationSystem getResearch16_publicationsystem() {
        return research16_publicationsystem;
    }

    public void setResearch16_publicationsystem(research16_PublicationSystem research16_publicationsystem) {
        this.research16_publicationsystem = research16_publicationsystem;
    }

}