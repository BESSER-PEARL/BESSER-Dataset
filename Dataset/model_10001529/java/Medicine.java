





import java.util.List;
import java.util.ArrayList;

public class Medicine  {

    private String potency;
    private String formula;
    private String name;
    private int id;





    private Product product;


    public Medicine(
        String potency,        String formula,        String name,        int id    ) {
        this.potency = potency;
        this.formula = formula;
        this.name = name;
        this.id = id;
    }


    public String getPotency() {
        return potency;
    }

    public void setPotency(String potency) {
        this.potency = potency;
    }
    public String getFormula() {
        return formula;
    }

    public void setFormula(String formula) {
        this.formula = formula;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}