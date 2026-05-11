





import java.util.List;
import java.util.ArrayList;

public class aml_Feature  {

    private String value;
    private String name;





    private aml_PriceRule aml_pricerule;


    public aml_Feature(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public aml_PriceRule getAml_pricerule() {
        return aml_pricerule;
    }

    public void setAml_pricerule(aml_PriceRule aml_pricerule) {
        this.aml_pricerule = aml_pricerule;
    }

}