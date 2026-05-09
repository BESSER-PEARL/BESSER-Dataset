





import java.util.List;
import java.util.ArrayList;

public class UML2_Class extends BehavioredClassifier, EncapsulatedClassifier {

    private boolean isActive;





    private UML2_Class uml2_class;


    public UML2_Class(
        boolean isActive    ) {
        super(
        );
        this.isActive = isActive;
    }


    public boolean getIsactive() {
        return isActive;
    }

    public void setIsactive(boolean isActive) {
        this.isActive = isActive;
    }

    public UML2_Class getUml2_class() {
        return uml2_class;
    }

    public void setUml2_class(UML2_Class uml2_class) {
        this.uml2_class = uml2_class;
    }

}