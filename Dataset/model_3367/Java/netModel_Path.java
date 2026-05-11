





import java.util.List;
import java.util.ArrayList;

public class netModel_Path  {

    private String arb;





    private List<netModel_SimpleMemberAssignment> netmodel_simplememberassignments;




    private netModel_HttpMethod netmodel_httpmethod;


    public netModel_Path(
        String arb    ) {
        this.arb = arb;
        this.netmodel_simplememberassignments = new ArrayList<>();
    }

    public netModel_Path(
        String arb        ArrayList<netModel_SimpleMemberAssignment> netmodel_simplememberassignments    ) {
        this.arb = arb;
        this.netmodel_simplememberassignments = netmodel_simplememberassignments;
    }

    public String getArb() {
        return arb;
    }

    public void setArb(String arb) {
        this.arb = arb;
    }

    public List<netModel_SimpleMemberAssignment> getNetmodel_simplememberassignments() {
        return netmodel_simplememberassignments;
    }

    public void addNetmodel_simplememberassignment(Netmodel_simplememberassignment netmodel_simplememberassignment) {
        this.netmodel_simplememberassignments.add(netmodel_simplememberassignment);
    }
    public netModel_HttpMethod getNetmodel_httpmethod() {
        return netmodel_httpmethod;
    }

    public void setNetmodel_httpmethod(netModel_HttpMethod netmodel_httpmethod) {
        this.netmodel_httpmethod = netmodel_httpmethod;
    }

}