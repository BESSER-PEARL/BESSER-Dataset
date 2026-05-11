





import java.util.List;
import java.util.ArrayList;

public class model_VAT extends IEntity {

    private String description;
    private String taxValue;
    private String salesEqualizationTax;



    public model_VAT(
        String description,        String taxValue,        String salesEqualizationTax    ) {
        super(
        );
        this.description = description;
        this.taxValue = taxValue;
        this.salesEqualizationTax = salesEqualizationTax;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTaxvalue() {
        return taxValue;
    }

    public void setTaxvalue(String taxValue) {
        this.taxValue = taxValue;
    }
    public String getSalesequalizationtax() {
        return salesEqualizationTax;
    }

    public void setSalesequalizationtax(String salesEqualizationTax) {
        this.salesEqualizationTax = salesEqualizationTax;
    }


}