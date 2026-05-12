





import java.util.List;
import java.util.ArrayList;

public class Shipment  {

    private String name;





    private List<Warehouse> warehouses;


    public Shipment(
        String name    ) {
        this.name = name;
        this.warehouses = new ArrayList<>();
    }

    public Shipment(
        String name        ArrayList<Warehouse> warehouses    ) {
        this.name = name;
        this.warehouses = warehouses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Warehouse> getWarehouses() {
        return warehouses;
    }

    public void addWarehouse(Warehouse warehouse) {
        this.warehouses.add(warehouse);
    }

}