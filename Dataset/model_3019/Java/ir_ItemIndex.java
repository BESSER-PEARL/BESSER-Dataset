





import java.util.List;
import java.util.ArrayList;

public class ir_ItemIndex extends IrAnnotable {

    private String itemName;
    private String name;



    public ir_ItemIndex(
        String itemName,        String name    ) {
        super(
        );
        this.itemName = itemName;
        this.name = name;
    }


    public String getItemname() {
        return itemName;
    }

    public void setItemname(String itemName) {
        this.itemName = itemName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}