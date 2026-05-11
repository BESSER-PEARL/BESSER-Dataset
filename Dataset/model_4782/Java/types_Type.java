





import java.util.List;
import java.util.ArrayList;

public class types_Type extends PackageMember {

    private boolean abstract;





    private types_TypedElement types_typedelement;




    private types_TypeParameter types_typeparameter;




    private types_TypedElement types_typedelement;


    public types_Type(
        boolean abstract    ) {
        super(
        );
        this.abstract = abstract;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public types_TypedElement getTypes_typedelement() {
        return types_typedelement;
    }

    public void setTypes_typedelement(types_TypedElement types_typedelement) {
        this.types_typedelement = types_typedelement;
    }
    public types_TypeParameter getTypes_typeparameter() {
        return types_typeparameter;
    }

    public void setTypes_typeparameter(types_TypeParameter types_typeparameter) {
        this.types_typeparameter = types_typeparameter;
    }
    public types_TypedElement getTypes_typedelement() {
        return types_typedelement;
    }

    public void setTypes_typedelement(types_TypedElement types_typedelement) {
        this.types_typedelement = types_typedelement;
    }

}