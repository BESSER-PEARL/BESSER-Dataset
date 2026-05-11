





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDRedefinableComponent extends xsd_XSDNamedComponent, xsd_XSDRedefineContent {

    private boolean circular;



    public model_xsd_XSDRedefinableComponent(
        boolean circular    ) {
        super(
        );
        this.circular = circular;
    }


    public boolean getCircular() {
        return circular;
    }

    public void setCircular(boolean circular) {
        this.circular = circular;
    }


}