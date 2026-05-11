





import java.util.List;
import java.util.ArrayList;

public class operators_Operator extends Company {






    private List<operators_Warehouse> operators_warehouses;




    private List<operators_ResourceExpansion> operators_resourceexpansions;




    private List<operators_Network> operators_networks;


    public operators_Operator(
    ) {
        super(
        );
        this.operators_warehouses = new ArrayList<>();
        this.operators_resourceexpansions = new ArrayList<>();
        this.operators_networks = new ArrayList<>();
    }

    public operators_Operator(
        ArrayList<operators_Warehouse> operators_warehouses,        ArrayList<operators_ResourceExpansion> operators_resourceexpansions,        ArrayList<operators_Network> operators_networks    ) {
        this.operators_warehouses = operators_warehouses;
        this.operators_resourceexpansions = operators_resourceexpansions;
        this.operators_networks = operators_networks;
    }


    public List<operators_Warehouse> getOperators_warehouses() {
        return operators_warehouses;
    }

    public void addOperators_warehouse(Operators_warehouse operators_warehouse) {
        this.operators_warehouses.add(operators_warehouse);
    }
    public List<operators_ResourceExpansion> getOperators_resourceexpansions() {
        return operators_resourceexpansions;
    }

    public void addOperators_resourceexpansion(Operators_resourceexpansion operators_resourceexpansion) {
        this.operators_resourceexpansions.add(operators_resourceexpansion);
    }
    public List<operators_Network> getOperators_networks() {
        return operators_networks;
    }

    public void addOperators_network(Operators_network operators_network) {
        this.operators_networks.add(operators_network);
    }

}