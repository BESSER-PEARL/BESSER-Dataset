





import java.util.List;
import java.util.ArrayList;

public class emfta_Gate  {

    private int nbOccurrences;
    private String type;
    private String description;





    private List<emfta_Event> emfta_events;




    private emfta_Event emfta_event;


    public emfta_Gate(
        int nbOccurrences,        String type,        String description    ) {
        this.nbOccurrences = nbOccurrences;
        this.type = type;
        this.description = description;
        this.emfta_events = new ArrayList<>();
    }

    public emfta_Gate(
        int nbOccurrences,        String type,        String description        ArrayList<emfta_Event> emfta_events    ) {
        this.nbOccurrences = nbOccurrences;
        this.type = type;
        this.description = description;
        this.emfta_events = emfta_events;
    }

    public int getNboccurrences() {
        return nbOccurrences;
    }

    public void setNboccurrences(int nbOccurrences) {
        this.nbOccurrences = nbOccurrences;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<emfta_Event> getEmfta_events() {
        return emfta_events;
    }

    public void addEmfta_event(Emfta_event emfta_event) {
        this.emfta_events.add(emfta_event);
    }
    public emfta_Event getEmfta_event() {
        return emfta_event;
    }

    public void setEmfta_event(emfta_Event emfta_event) {
        this.emfta_event = emfta_event;
    }

}