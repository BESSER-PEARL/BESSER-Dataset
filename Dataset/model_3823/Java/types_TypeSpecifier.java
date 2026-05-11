





import java.util.List;
import java.util.ArrayList;

public class types_TypeSpecifier  {






    private types_TypedElement types_typedelement;




    private List<types_TypeSpecifier> types_typespecifiers;


    public types_TypeSpecifier(
    ) {
        this.types_typespecifiers = new ArrayList<>();
    }

    public types_TypeSpecifier(
        ArrayList<types_TypeSpecifier> types_typespecifiers    ) {
        this.types_typespecifiers = types_typespecifiers;
    }


    public types_TypedElement getTypes_typedelement() {
        return types_typedelement;
    }

    public void setTypes_typedelement(types_TypedElement types_typedelement) {
        this.types_typedelement = types_typedelement;
    }
    public List<types_TypeSpecifier> getTypes_typespecifiers() {
        return types_typespecifiers;
    }

    public void addTypes_typespecifier(Types_typespecifier types_typespecifier) {
        this.types_typespecifiers.add(types_typespecifier);
    }

}