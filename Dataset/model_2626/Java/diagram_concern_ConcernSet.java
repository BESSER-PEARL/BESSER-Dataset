





import java.util.List;
import java.util.ArrayList;

public class diagram_concern_ConcernSet extends DocumentedElement {






    private List<concern_ConcernDescription> concern_concerndescriptions;


    public diagram_concern_ConcernSet(
    ) {
        super(
        );
        this.concern_concerndescriptions = new ArrayList<>();
    }

    public diagram_concern_ConcernSet(
        ArrayList<concern_ConcernDescription> concern_concerndescriptions    ) {
        this.concern_concerndescriptions = concern_concerndescriptions;
    }


    public List<concern_ConcernDescription> getConcern_concerndescriptions() {
        return concern_concerndescriptions;
    }

    public void addConcern_concerndescription(Concern_concerndescription concern_concerndescription) {
        this.concern_concerndescriptions.add(concern_concerndescription);
    }

}