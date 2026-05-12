





import java.util.List;
import java.util.ArrayList;

public class Supply  {

    private float cost_per_unit;
    private int reorder_level;
    private String description;
    private int num;
    private int stock;
    private String name;





    private List<Requisition> requisitions;


    public Supply(
        float cost_per_unit,        int reorder_level,        String description,        int num,        int stock,        String name    ) {
        this.cost_per_unit = cost_per_unit;
        this.reorder_level = reorder_level;
        this.description = description;
        this.num = num;
        this.stock = stock;
        this.name = name;
        this.requisitions = new ArrayList<>();
    }

    public Supply(
        float cost_per_unit,        int reorder_level,        String description,        int num,        int stock,        String name        ArrayList<Requisition> requisitions    ) {
        this.cost_per_unit = cost_per_unit;
        this.reorder_level = reorder_level;
        this.description = description;
        this.num = num;
        this.stock = stock;
        this.name = name;
        this.requisitions = requisitions;
    }

    public float getCost_per_unit() {
        return cost_per_unit;
    }

    public void setCost_per_unit(float cost_per_unit) {
        this.cost_per_unit = cost_per_unit;
    }
    public int getReorder_level() {
        return reorder_level;
    }

    public void setReorder_level(int reorder_level) {
        this.reorder_level = reorder_level;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }
    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Requisition> getRequisitions() {
        return requisitions;
    }

    public void addRequisition(Requisition requisition) {
        this.requisitions.add(requisition);
    }

}