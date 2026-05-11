





import java.util.List;
import java.util.ArrayList;

public class BPMNProfile_ResourceParameter extends BaseElement {

    private String isRequired;



    public BPMNProfile_ResourceParameter(
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