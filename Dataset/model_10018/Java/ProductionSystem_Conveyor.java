





import java.util.List;
import java.util.ArrayList;

public class ProductionSystem_Conveyor  {

    private String id;
    private int capacity;





    private ProductionSystem_Machine productionsystem_machine;




    private ProductionSystem_Conveyor productionsystem_conveyor;




    private ProductionSystem_Machine productionsystem_machine;




    private ProductionSystem_Machine productionsystem_machine;




    private List<ProductionSystem_Conveyor> productionsystem_conveyors;




    private ProductionSystem_Machine productionsystem_machine;


    public ProductionSystem_Conveyor(
        String id,        int capacity    ) {
        this.id = id;
        this.capacity = capacity;
        this.productionsystem_conveyors = new ArrayList<>();
    }

    public ProductionSystem_Conveyor(
        String id,        int capacity        ArrayList<ProductionSystem_Conveyor> productionsystem_conveyors    ) {
        this.id = id;
        this.capacity = capacity;
        this.productionsystem_conveyors = productionsystem_conveyors;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public ProductionSystem_Machine getProductionsystem_machine() {
        return productionsystem_machine;
    }

    public void setProductionsystem_machine(ProductionSystem_Machine productionsystem_machine) {
        this.productionsystem_machine = productionsystem_machine;
    }
    public ProductionSystem_Conveyor getProductionsystem_conveyor() {
        return productionsystem_conveyor;
    }

    public void setProductionsystem_conveyor(ProductionSystem_Conveyor productionsystem_conveyor) {
        this.productionsystem_conveyor = productionsystem_conveyor;
    }
    public ProductionSystem_Machine getProductionsystem_machine() {
        return productionsystem_machine;
    }

    public void setProductionsystem_machine(ProductionSystem_Machine productionsystem_machine) {
        this.productionsystem_machine = productionsystem_machine;
    }
    public ProductionSystem_Machine getProductionsystem_machine() {
        return productionsystem_machine;
    }

    public void setProductionsystem_machine(ProductionSystem_Machine productionsystem_machine) {
        this.productionsystem_machine = productionsystem_machine;
    }
    public List<ProductionSystem_Conveyor> getProductionsystem_conveyors() {
        return productionsystem_conveyors;
    }

    public void addProductionsystem_conveyor(Productionsystem_conveyor productionsystem_conveyor) {
        this.productionsystem_conveyors.add(productionsystem_conveyor);
    }
    public ProductionSystem_Machine getProductionsystem_machine() {
        return productionsystem_machine;
    }

    public void setProductionsystem_machine(ProductionSystem_Machine productionsystem_machine) {
        this.productionsystem_machine = productionsystem_machine;
    }

}