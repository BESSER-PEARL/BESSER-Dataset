





import java.util.List;
import java.util.ArrayList;

public class model_Link extends DiagramElement, FeatureContainer {

    private boolean complex;
    private boolean reference;



    public model_Link(
        boolean complex,        boolean reference    ) {
        super(
        );
        this.complex = complex;
        this.reference = reference;
    }


    public boolean getComplex() {
        return complex;
    }

    public void setComplex(boolean complex) {
        this.complex = complex;
    }
    public boolean getReference() {
        return reference;
    }

    public void setReference(boolean reference) {
        this.reference = reference;
    }


}