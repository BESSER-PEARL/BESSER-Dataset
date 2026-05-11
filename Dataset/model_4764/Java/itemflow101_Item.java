





import java.util.List;
import java.util.ArrayList;

public class itemflow101_Item  {

    private String name;





    private itemflow101_Flow itemflow101_flow;


    public itemflow101_Item(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public itemflow101_Flow getItemflow101_flow() {
        return itemflow101_flow;
    }

    public void setItemflow101_flow(itemflow101_Flow itemflow101_flow) {
        this.itemflow101_flow = itemflow101_flow;
    }

}