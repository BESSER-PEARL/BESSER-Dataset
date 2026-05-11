





import java.util.List;
import java.util.ArrayList;

public class ram_ImplementationClass extends Classifier {

    private boolean interface;
    private String instanceClassName;



    public ram_ImplementationClass(
        boolean interface,        String instanceClassName    ) {
        super(
        );
        this.interface = interface;
        this.instanceClassName = instanceClassName;
    }


    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }
    public String getInstanceclassname() {
        return instanceClassName;
    }

    public void setInstanceclassname(String instanceClassName) {
        this.instanceClassName = instanceClassName;
    }


}