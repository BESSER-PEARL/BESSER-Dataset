





import java.util.List;
import java.util.ArrayList;

public class ir_ItemId extends IrAnnotable {

    private String name;
    private String itemName;





    private ir_ItemIndexValue ir_itemindexvalue;


    public ir_ItemId(
        String name,        String itemName    ) {
        super(
        );
        this.name = name;
        this.itemName = itemName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getItemname() {
        return itemName;
    }

    public void setItemname(String itemName) {
        this.itemName = itemName;
    }

    public ir_ItemIndexValue getIr_itemindexvalue() {
        return ir_itemindexvalue;
    }

    public void setIr_itemindexvalue(ir_ItemIndexValue ir_itemindexvalue) {
        this.ir_itemindexvalue = ir_itemindexvalue;
    }

}