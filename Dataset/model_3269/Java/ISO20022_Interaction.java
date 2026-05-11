





import java.util.List;
import java.util.ArrayList;

public class ISO20022_Interaction extends RepositoryConcept {

    private String location;





    private ISO20022_Diagram iso20022_diagram;




    private ISO20022_InteractionActor iso20022_interactionactor;




    private List<ISO20022_InteractionActor> iso20022_interactionactors;


    public ISO20022_Interaction(
        String location    ) {
        super(
        );
        this.location = location;
        this.iso20022_interactionactors = new ArrayList<>();
    }

    public ISO20022_Interaction(
        String location        ArrayList<ISO20022_InteractionActor> iso20022_interactionactors    ) {
        this.location = location;
        this.iso20022_interactionactors = iso20022_interactionactors;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public ISO20022_Diagram getIso20022_diagram() {
        return iso20022_diagram;
    }

    public void setIso20022_diagram(ISO20022_Diagram iso20022_diagram) {
        this.iso20022_diagram = iso20022_diagram;
    }
    public ISO20022_InteractionActor getIso20022_interactionactor() {
        return iso20022_interactionactor;
    }

    public void setIso20022_interactionactor(ISO20022_InteractionActor iso20022_interactionactor) {
        this.iso20022_interactionactor = iso20022_interactionactor;
    }
    public List<ISO20022_InteractionActor> getIso20022_interactionactors() {
        return iso20022_interactionactors;
    }

    public void addIso20022_interactionactor(Iso20022_interactionactor iso20022_interactionactor) {
        this.iso20022_interactionactors.add(iso20022_interactionactor);
    }

}