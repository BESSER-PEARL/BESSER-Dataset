





import java.util.List;
import java.util.ArrayList;

public class UML2_TimeTrigger extends Trigger {

    private boolean isRelative;





    private UML2_ValueSpecification uml2_valuespecification;


    public UML2_TimeTrigger(
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

    public UML2_ValueSpecification getUml2_valuespecification() {
        return uml2_valuespecification;
    }

    public void setUml2_valuespecification(UML2_ValueSpecification uml2_valuespecification) {
        this.uml2_valuespecification = uml2_valuespecification;
    }

}