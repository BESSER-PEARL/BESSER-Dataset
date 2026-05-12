





import java.util.List;
import java.util.ArrayList;

public class Shipment  {

    private String packing;





    private List<sellers_warehouse> sellers_warehouses;


    public Shipment(
        String packing    ) {
        this.packing = packing;
        this.sellers_warehouses = new ArrayList<>();
    }

    public Shipment(
        String packing        ArrayList<sellers_warehouse> sellers_warehouses    ) {
        this.packing = packing;
        this.sellers_warehouses = sellers_warehouses;
    }

    public String getPacking() {
        return packing;
    }

    public void setPacking(String packing) {
        this.packing = packing;
    }

    public List<sellers_warehouse> getSellers_warehouses() {
        return sellers_warehouses;
    }

    public void addSellers_warehouse(Sellers_warehouse sellers_warehouse) {
        this.sellers_warehouses.add(sellers_warehouse);
    }

}