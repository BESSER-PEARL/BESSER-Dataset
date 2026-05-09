





import java.util.List;
import java.util.ArrayList;

public class research23_PublicationStatus  {

    private String label;





    private research23_PublicationStructure research23_publicationstructure;




    private List<research23_State> research23_states;


    public research23_PublicationStatus(
        String label    ) {
        this.label = label;
        this.research23_states = new ArrayList<>();
    }

    public research23_PublicationStatus(
        String label        ArrayList<research23_State> research23_states    ) {
        this.label = label;
        this.research23_states = research23_states;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public research23_PublicationStructure getResearch23_publicationstructure() {
        return research23_publicationstructure;
    }

    public void setResearch23_publicationstructure(research23_PublicationStructure research23_publicationstructure) {
        this.research23_publicationstructure = research23_publicationstructure;
    }
    public List<research23_State> getResearch23_states() {
        return research23_states;
    }

    public void addResearch23_state(Research23_state research23_state) {
        this.research23_states.add(research23_state);
    }

}