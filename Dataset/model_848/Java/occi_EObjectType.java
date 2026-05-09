





import java.util.List;
import java.util.ArrayList;

public class occi_EObjectType extends BasicType {

    private String instanceClassName;



    public occi_EObjectType(
        String instanceClassName    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
    }


    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }


}