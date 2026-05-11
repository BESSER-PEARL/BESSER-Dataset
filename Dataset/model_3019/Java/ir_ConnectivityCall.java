





import java.util.List;
import java.util.ArrayList;

public class ir_ConnectivityCall extends Container {






    private ir_Connectivity ir_connectivity;




    private ir_ItemIndexValue ir_itemindexvalue;




    private List<ir_ItemId> ir_itemids;




    private ir_SetDefinition ir_setdefinition;


    public ir_ConnectivityCall(
    ) {
        super(
        );
        this.ir_itemids = new ArrayList<>();
    }

    public ir_ConnectivityCall(
        ArrayList<ir_ItemId> ir_itemids    ) {
        this.ir_itemids = ir_itemids;
    }


    public ir_Connectivity getIr_connectivity() {
        return ir_connectivity;
    }

    public void setIr_connectivity(ir_Connectivity ir_connectivity) {
        this.ir_connectivity = ir_connectivity;
    }
    public ir_ItemIndexValue getIr_itemindexvalue() {
        return ir_itemindexvalue;
    }

    public void setIr_itemindexvalue(ir_ItemIndexValue ir_itemindexvalue) {
        this.ir_itemindexvalue = ir_itemindexvalue;
    }
    public List<ir_ItemId> getIr_itemids() {
        return ir_itemids;
    }

    public void addIr_itemid(Ir_itemid ir_itemid) {
        this.ir_itemids.add(ir_itemid);
    }
    public ir_SetDefinition getIr_setdefinition() {
        return ir_setdefinition;
    }

    public void setIr_setdefinition(ir_SetDefinition ir_setdefinition) {
        this.ir_setdefinition = ir_setdefinition;
    }

}