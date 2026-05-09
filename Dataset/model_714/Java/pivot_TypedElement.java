





import java.util.List;
import java.util.ArrayList;

public class pivot_TypedElement extends NamedElement {

    private String isRequired;



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


}