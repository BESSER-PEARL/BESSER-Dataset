





import java.util.List;
import java.util.ArrayList;

public class ir_Connectivity extends IrAnnotable {

    private boolean multiple;
    private boolean indexEqualId;
    private String name;





    private ir_ItemType ir_itemtype;




    private List<ir_ItemType> ir_itemtypes;


    public ir_Connectivity(
        boolean multiple,        boolean indexEqualId,        String name    ) {
        super(
        );
        this.multiple = multiple;
        this.indexEqualId = indexEqualId;
        this.name = name;
        this.ir_itemtypes = new ArrayList<>();
    }

    public ir_Connectivity(
        boolean multiple,        boolean indexEqualId,        String name        ArrayList<ir_ItemType> ir_itemtypes    ) {
        this.multiple = multiple;
        this.indexEqualId = indexEqualId;
        this.name = name;
        this.ir_itemtypes = ir_itemtypes;
    }

    public boolean getMultiple() {
        return multiple;
    }

    public void setMultiple(boolean multiple) {
        this.multiple = multiple;
    }
    public boolean getIndexequalid() {
        return indexEqualId;
    }

    public void setIndexequalid(boolean indexEqualId) {
        this.indexEqualId = indexEqualId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ir_ItemType getIr_itemtype() {
        return ir_itemtype;
    }

    public void setIr_itemtype(ir_ItemType ir_itemtype) {
        this.ir_itemtype = ir_itemtype;
    }
    public List<ir_ItemType> getIr_itemtypes() {
        return ir_itemtypes;
    }

    public void addIr_itemtype(Ir_itemtype ir_itemtype) {
        this.ir_itemtypes.add(ir_itemtype);
    }

}