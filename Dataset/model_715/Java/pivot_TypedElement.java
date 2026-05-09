





import java.util.List;
import java.util.ArrayList;

public class pivot_TypedElement extends NamedElement {

    private String isMany;
    private String isRequired;



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


}