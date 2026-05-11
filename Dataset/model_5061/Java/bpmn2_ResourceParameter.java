





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ResourceParameter extends BaseElement {

    private String name;
    private boolean isRequired;



    public bpmn2_ResourceParameter(
        String name,        boolean isRequired    ) {
        super(
        );
        this.name = name;
        this.isRequired = isRequired;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(boolean isRequired) {
        this.isRequired = isRequired;
    }


}