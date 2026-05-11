





import java.util.List;
import java.util.ArrayList;

public class itemflow101_OutputPort extends Port {






    private List<itemflow101_Flow> itemflow101_flows;




    private itemflow101_Function itemflow101_function;


    public itemflow101_OutputPort(
    ) {
        super(
        );
        this.itemflow101_flows = new ArrayList<>();
    }

    public itemflow101_OutputPort(
        ArrayList<itemflow101_Flow> itemflow101_flows    ) {
        this.itemflow101_flows = itemflow101_flows;
    }


    public List<itemflow101_Flow> getItemflow101_flows() {
        return itemflow101_flows;
    }

    public void addItemflow101_flow(Itemflow101_flow itemflow101_flow) {
        this.itemflow101_flows.add(itemflow101_flow);
    }
    public itemflow101_Function getItemflow101_function() {
        return itemflow101_function;
    }

    public void setItemflow101_function(itemflow101_Function itemflow101_function) {
        this.itemflow101_function = itemflow101_function;
    }

}