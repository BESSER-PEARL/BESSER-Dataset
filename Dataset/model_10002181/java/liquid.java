





import java.util.List;
import java.util.ArrayList;

public class liquid  {

    private String must_be_unit_in_ml;
    private String quantiy;
    private String name;





    private Component component;


    public liquid(
        String must_be_unit_in_ml,        String quantiy,        String name    ) {
        this.must_be_unit_in_ml = must_be_unit_in_ml;
        this.quantiy = quantiy;
        this.name = name;
    }


    public String getMust_be_unit_in_ml() {
        return must_be_unit_in_ml;
    }

    public void setMust_be_unit_in_ml(String must_be_unit_in_ml) {
        this.must_be_unit_in_ml = must_be_unit_in_ml;
    }
    public String getQuantiy() {
        return quantiy;
    }

    public void setQuantiy(String quantiy) {
        this.quantiy = quantiy;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Component getComponent() {
        return component;
    }

    public void setComponent(Component component) {
        this.component = component;
    }

}