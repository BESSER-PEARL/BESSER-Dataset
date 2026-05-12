





import java.util.List;
import java.util.ArrayList;

public class research32_PublicationStatus  {

    private String label;





    private List<research32_State> research32_states;




    private research32_PublicationStructure research32_publicationstructure;


    public research32_PublicationStatus(
        String label    ) {
        this.label = label;
        this.research32_states = new ArrayList<>();
    }

    public research32_PublicationStatus(
        String label        ArrayList<research32_State> research32_states    ) {
        this.label = label;
        this.research32_states = research32_states;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<research32_State> getResearch32_states() {
        return research32_states;
    }

    public void addResearch32_state(Research32_state research32_state) {
        this.research32_states.add(research32_state);
    }
    public research32_PublicationStructure getResearch32_publicationstructure() {
        return research32_publicationstructure;
    }

    public void setResearch32_publicationstructure(research32_PublicationStructure research32_publicationstructure) {
        this.research32_publicationstructure = research32_publicationstructure;
    }

}