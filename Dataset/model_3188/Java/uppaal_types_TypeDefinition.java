





import java.util.List;
import java.util.ArrayList;

public class uppaal_types_TypeDefinition  {

    private String baseType;





    private TypeSpecification typespecification;


    public uppaal_types_TypeDefinition(
        String baseType    ) {
        this.baseType = baseType;
    }


    public String getBasetype() {
        return baseType;
    }

    public void setBasetype(String baseType) {
        this.baseType = baseType;
    }

    public TypeSpecification getTypespecification() {
        return typespecification;
    }

    public void setTypespecification(TypeSpecification typespecification) {
        this.typespecification = typespecification;
    }

}