





import java.util.List;
import java.util.ArrayList;

public class types_Type extends PackageMember {

    private boolean abstract;
    private boolean visible;





    private types_TypeSpecifier types_typespecifier;




    private types_TypedElement types_typedelement;


    public types_Type(
        boolean abstract,        boolean visible    ) {
        super(
        );
        this.abstract = abstract;
        this.visible = visible;
    }


    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }

    public types_TypeSpecifier getTypes_typespecifier() {
        return types_typespecifier;
    }

    public void setTypes_typespecifier(types_TypeSpecifier types_typespecifier) {
        this.types_typespecifier = types_typespecifier;
    }
    public types_TypedElement getTypes_typedelement() {
        return types_typedelement;
    }

    public void setTypes_typedelement(types_TypedElement types_typedelement) {
        this.types_typedelement = types_typedelement;
    }

}