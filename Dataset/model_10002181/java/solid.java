





import java.util.List;
import java.util.ArrayList;

public class solid  {

    private String must_be_unit_in_kg;





    private Component component;


    public solid(
        String must_be_unit_in_kg    ) {
        this.must_be_unit_in_kg = must_be_unit_in_kg;
    }


    public String getMust_be_unit_in_kg() {
        return must_be_unit_in_kg;
    }

    public void setMust_be_unit_in_kg(String must_be_unit_in_kg) {
        this.must_be_unit_in_kg = must_be_unit_in_kg;
    }

    public Component getComponent() {
        return component;
    }

    public void setComponent(Component component) {
        this.component = component;
    }

}