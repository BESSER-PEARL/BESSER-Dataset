





import java.util.List;
import java.util.ArrayList;

public class ram_ImplementationClass extends Classifier {

    private String instanceClassName;
    private boolean interface;



    public ram_ImplementationClass(
        String instanceClassName,        boolean interface    ) {
        super(
        );
        this.instanceClassName = instanceClassName;
        this.interface = interface;
    }


    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }
    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }


}