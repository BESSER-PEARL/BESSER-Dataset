





import java.util.List;
import java.util.ArrayList;

public class art_instance_ComponentInstance extends ModelElement {

    private String state;





    private ComponentType componenttype;


    public art_instance_ComponentInstance(
        String state    ) {
        super(
        );
        this.state = state;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public ComponentType getComponenttype() {
        return componenttype;
    }

    public void setComponenttype(ComponentType componenttype) {
        this.componenttype = componenttype;
    }

}