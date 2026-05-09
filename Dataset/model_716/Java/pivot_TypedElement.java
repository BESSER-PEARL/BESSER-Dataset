





import java.util.List;
import java.util.ArrayList;

public class pivot_TypedElement extends NamedElement {

    private String isRequired;
    private String isMany;



    public pivot_TypedElement(
        String isRequired,        String isMany    ) {
        super(
        );
        this.isRequired = isRequired;
        this.isMany = isMany;
    }


    public String getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(String isRequired) {
        this.isRequired = isRequired;
    }
    public String getIsmany() {
        return isMany;
    }

    public void setIsmany(String isMany) {
        this.isMany = isMany;
    }


}