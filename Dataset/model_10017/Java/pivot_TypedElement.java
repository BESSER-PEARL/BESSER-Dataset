





import java.util.List;
import java.util.ArrayList;

public class pivot_TypedElement extends NamedElement {

    private String isMany;
    private String isRequired;





    private pivot_Type pivot_type;


    public pivot_TypedElement(
        String isMany,        String isRequired    ) {
        super(
        );
        this.isMany = isMany;
        this.isRequired = isRequired;
    }


    public String getIsmany() {
        return isMany;
    }

    public void setIsmany(String isMany) {
        this.isMany = isMany;
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