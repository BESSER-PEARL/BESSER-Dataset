





import java.util.List;
import java.util.ArrayList;

public class UML_LiteralUnlimitedNatural extends Package {

    private int value;





    private UML_TypedElement uml_typedelement;


    public UML_LiteralUnlimitedNatural(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public UML_TypedElement getUml_typedelement() {
        return uml_typedelement;
    }

    public void setUml_typedelement(UML_TypedElement uml_typedelement) {
        this.uml_typedelement = uml_typedelement;
    }

}