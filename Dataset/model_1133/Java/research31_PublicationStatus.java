





import java.util.List;
import java.util.ArrayList;

public class research31_PublicationStatus  {

    private String label;





    private research31_PublicationStructure research31_publicationstructure;




    private List<research31_State> research31_states;


    public research31_PublicationStatus(
        String label    ) {
        this.label = label;
        this.research31_states = new ArrayList<>();
    }

    public research31_PublicationStatus(
        String label        ArrayList<research31_State> research31_states    ) {
        this.label = label;
        this.research31_states = research31_states;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public research31_PublicationStructure getResearch31_publicationstructure() {
        return research31_publicationstructure;
    }

    public void setResearch31_publicationstructure(research31_PublicationStructure research31_publicationstructure) {
        this.research31_publicationstructure = research31_publicationstructure;
    }
    public List<research31_State> getResearch31_states() {
        return research31_states;
    }

    public void addResearch31_state(Research31_state research31_state) {
        this.research31_states.add(research31_state);
    }

}