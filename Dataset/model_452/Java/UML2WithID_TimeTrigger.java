





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_TimeTrigger extends Trigger {

    private boolean isRelative;





    private UML2WithID_ValueSpecification uml2withid_valuespecification;


    public UML2WithID_TimeTrigger(
        boolean isRelative    ) {
        super(
        );
        this.isRelative = isRelative;
    }


    public boolean getIsrelative() {
        return isRelative;
    }

    public void setIsrelative(boolean isRelative) {
        this.isRelative = isRelative;
    }

    public UML2WithID_ValueSpecification getUml2withid_valuespecification() {
        return uml2withid_valuespecification;
    }

    public void setUml2withid_valuespecification(UML2WithID_ValueSpecification uml2withid_valuespecification) {
        this.uml2withid_valuespecification = uml2withid_valuespecification;
    }

}