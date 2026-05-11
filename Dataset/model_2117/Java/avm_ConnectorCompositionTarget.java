





import java.util.List;
import java.util.ArrayList;

public class avm_ConnectorCompositionTarget  {

    private String ID;





    private List<avm_ConnectorCompositionTarget> avm_connectorcompositiontargets;




    private List<avm_assemblyDetail> avm_assemblydetails;


    public avm_ConnectorCompositionTarget(
        String ID    ) {
        this.ID = ID;
        this.avm_connectorcompositiontargets = new ArrayList<>();
        this.avm_assemblydetails = new ArrayList<>();
    }

    public avm_ConnectorCompositionTarget(
        String ID        ArrayList<avm_ConnectorCompositionTarget> avm_connectorcompositiontargets,        ArrayList<avm_assemblyDetail> avm_assemblydetails    ) {
        this.ID = ID;
        this.avm_connectorcompositiontargets = avm_connectorcompositiontargets;
        this.avm_assemblydetails = avm_assemblydetails;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public List<avm_ConnectorCompositionTarget> getAvm_connectorcompositiontargets() {
        return avm_connectorcompositiontargets;
    }

    public void addAvm_connectorcompositiontarget(Avm_connectorcompositiontarget avm_connectorcompositiontarget) {
        this.avm_connectorcompositiontargets.add(avm_connectorcompositiontarget);
    }
    public List<avm_assemblyDetail> getAvm_assemblydetails() {
        return avm_assemblydetails;
    }

    public void addAvm_assemblydetail(Avm_assemblydetail avm_assemblydetail) {
        this.avm_assemblydetails.add(avm_assemblydetail);
    }

}