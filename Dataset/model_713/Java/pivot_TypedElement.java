





import java.util.List;
import java.util.ArrayList;

public class pivot_TypedElement extends NamedElement {

    private String isRequired;





    private pivot_Type pivot_type;


    public pivot_TypedElement(
        String isRequired    ) {
        super(
        );
        this.isRequired = isRequired;
    }


    public String getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(String isRequired) {
        this.isRequired = isRequired;
    }

    public pivot_Type getPivot_type() {
        return pivot_type;
    }

    public void setPivot_type(pivot_Type pivot_type) {
        this.pivot_type = pivot_type;
    }

}