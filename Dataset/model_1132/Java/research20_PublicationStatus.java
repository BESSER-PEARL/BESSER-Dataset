





import java.util.List;
import java.util.ArrayList;

public class research20_PublicationStatus  {

    private String label;





    private research20_PublicationStructure research20_publicationstructure;




    private List<research20_State> research20_states;


    public research20_PublicationStatus(
        String label    ) {
        this.label = label;
        this.research20_states = new ArrayList<>();
    }

    public research20_PublicationStatus(
        String label        ArrayList<research20_State> research20_states    ) {
        this.label = label;
        this.research20_states = research20_states;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public research20_PublicationStructure getResearch20_publicationstructure() {
        return research20_publicationstructure;
    }

    public void setResearch20_publicationstructure(research20_PublicationStructure research20_publicationstructure) {
        this.research20_publicationstructure = research20_publicationstructure;
    }
    public List<research20_State> getResearch20_states() {
        return research20_states;
    }

    public void addResearch20_state(Research20_state research20_state) {
        this.research20_states.add(research20_state);
    }

}