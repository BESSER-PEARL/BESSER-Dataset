





import java.util.List;
import java.util.ArrayList;

public class Warehouse  {

    private String Warehouse_branch;





    private List<Products> productss;


    public Warehouse(
        String Warehouse_branch    ) {
        this.Warehouse_branch = Warehouse_branch;
        this.productss = new ArrayList<>();
    }

    public Warehouse(
        String Warehouse_branch        ArrayList<Products> productss    ) {
        this.Warehouse_branch = Warehouse_branch;
        this.productss = productss;
    }

    public String getWarehouse_branch() {
        return Warehouse_branch;
    }

    public void setWarehouse_branch(String Warehouse_branch) {
        this.Warehouse_branch = Warehouse_branch;
    }

    public List<Products> getProductss() {
        return productss;
    }

    public void addProducts(Products products) {
        this.productss.add(products);
    }

}