





import java.util.List;
import java.util.ArrayList;

public class Shipment  {

    private String packing;





    private List<Warehouse> warehouses;


    public Shipment(
        String packing    ) {
        this.packing = packing;
        this.warehouses = new ArrayList<>();
    }

    public Shipment(
        String packing        ArrayList<Warehouse> warehouses    ) {
        this.packing = packing;
        this.warehouses = warehouses;
    }

    public String getPacking() {
        return packing;
    }

    public void setPacking(String packing) {
        this.packing = packing;
    }

    public List<Warehouse> getWarehouses() {
        return warehouses;
    }

    public void addWarehouse(Warehouse warehouse) {
        this.warehouses.add(warehouse);
    }

}