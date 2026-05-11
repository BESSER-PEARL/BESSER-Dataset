





import java.util.List;
import java.util.ArrayList;

public class netModel_ParamsBlock extends HttpMethodBlock, ClientBlock {






    private List<netModel_SimpleMemberAssignment> netmodel_simplememberassignments;


    public netModel_ParamsBlock(
    ) {
        super(
        );
        this.netmodel_simplememberassignments = new ArrayList<>();
    }

    public netModel_ParamsBlock(
        ArrayList<netModel_SimpleMemberAssignment> netmodel_simplememberassignments    ) {
        this.netmodel_simplememberassignments = netmodel_simplememberassignments;
    }


    public List<netModel_SimpleMemberAssignment> getNetmodel_simplememberassignments() {
        return netmodel_simplememberassignments;
    }

    public void addNetmodel_simplememberassignment(Netmodel_simplememberassignment netmodel_simplememberassignment) {
        this.netmodel_simplememberassignments.add(netmodel_simplememberassignment);
    }

}