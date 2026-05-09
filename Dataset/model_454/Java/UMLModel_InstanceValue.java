





import java.util.List;
import java.util.ArrayList;

public class UMLModel_InstanceValue extends ValueSpecification {

    private String instance;



    public UMLModel_InstanceValue(
        String instance    ) {
        super(
        );
        this.instance = instance;
    }


    public String getInstance() {
        return instance;
    }

    public void setInstance(String instance) {
        this.instance = instance;
    }


}