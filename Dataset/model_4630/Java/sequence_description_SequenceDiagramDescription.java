





import java.util.List;
import java.util.ArrayList;

public class sequence_description_SequenceDiagramDescription extends DiagramDescription {

    private String instanceRolesOrdering;
    private String endsOrdering;



    public sequence_description_SequenceDiagramDescription(
        String instanceRolesOrdering,        String endsOrdering    ) {
        super(
        );
        this.instanceRolesOrdering = instanceRolesOrdering;
        this.endsOrdering = endsOrdering;
    }


    public String getInstancerolesordering() {
        return instanceRolesOrdering;
    }

    public void setInstancerolesordering(String instanceRolesOrdering) {
        this.instanceRolesOrdering = instanceRolesOrdering;
    }
    public String getEndsordering() {
        return endsOrdering;
    }

    public void setEndsordering(String endsOrdering) {
        this.endsOrdering = endsOrdering;
    }


}