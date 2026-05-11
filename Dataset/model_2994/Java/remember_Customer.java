





import java.util.List;
import java.util.ArrayList;

public class remember_Customer  {

    private String name;
    private String customerId;





    private remember_Node remember_node;




    private List<remember_Node> remember_nodes;




    private remember_Customers remember_customers;


    public remember_Customer(
        String name,        String customerId    ) {
        this.name = name;
        this.customerId = customerId;
        this.remember_nodes = new ArrayList<>();
    }

    public remember_Customer(
        String name,        String customerId        ArrayList<remember_Node> remember_nodes    ) {
        this.name = name;
        this.customerId = customerId;
        this.remember_nodes = remember_nodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCustomerid() {
        return customerId;
    }

    public void setCustomerid(String customerId) {
        this.customerId = customerId;
    }

    public remember_Node getRemember_node() {
        return remember_node;
    }

    public void setRemember_node(remember_Node remember_node) {
        this.remember_node = remember_node;
    }
    public List<remember_Node> getRemember_nodes() {
        return remember_nodes;
    }

    public void addRemember_node(Remember_node remember_node) {
        this.remember_nodes.add(remember_node);
    }
    public remember_Customers getRemember_customers() {
        return remember_customers;
    }

    public void setRemember_customers(remember_Customers remember_customers) {
        this.remember_customers = remember_customers;
    }

}