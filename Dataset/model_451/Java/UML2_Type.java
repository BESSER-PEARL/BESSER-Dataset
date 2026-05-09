





import java.util.List;
import java.util.ArrayList;

public class UML2_Type extends PackageableElement {






    private UML2_TypedElement uml2_typedelement;




    private UML2_Association uml2_association;


    public UML2_Type(
    ) {
        super(
        );
    }



    public UML2_TypedElement getUml2_typedelement() {
        return uml2_typedelement;
    }

    public void setUml2_typedelement(UML2_TypedElement uml2_typedelement) {
        this.uml2_typedelement = uml2_typedelement;
    }
    public UML2_Association getUml2_association() {
        return uml2_association;
    }

    public void setUml2_association(UML2_Association uml2_association) {
        this.uml2_association = uml2_association;
    }

}