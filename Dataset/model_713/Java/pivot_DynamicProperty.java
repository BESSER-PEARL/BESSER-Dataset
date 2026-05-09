





import java.util.List;
import java.util.ArrayList;

public class pivot_DynamicProperty extends Element {

    private String default;





    private pivot_Property pivot_property;




    private pivot_DynamicType pivot_dynamictype;


    public pivot_DynamicProperty(
        String default    ) {
        super(
        );
        this.default = default;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public pivot_Property getPivot_property() {
        return pivot_property;
    }

    public void setPivot_property(pivot_Property pivot_property) {
        this.pivot_property = pivot_property;
    }
    public pivot_DynamicType getPivot_dynamictype() {
        return pivot_dynamictype;
    }

    public void setPivot_dynamictype(pivot_DynamicType pivot_dynamictype) {
        this.pivot_dynamictype = pivot_dynamictype;
    }

}