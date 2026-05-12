





import java.util.List;
import java.util.ArrayList;

public class Medicine  {

    private int id;
    private String name;
    private String formula;
    private String potency;





    private Product product;


    public Medicine(
        int id,        String name,        String formula,        String potency    ) {
        this.id = id;
        this.name = name;
        this.formula = formula;
        this.potency = potency;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFormula() {
        return formula;
    }

    public void setFormula(String formula) {
        this.formula = formula;
    }
    public String getPotency() {
        return potency;
    }

    public void setPotency(String potency) {
        this.potency = potency;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}