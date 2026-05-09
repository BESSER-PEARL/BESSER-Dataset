





import java.util.List;
import java.util.ArrayList;

public class astm_NamedTypeReference extends TypeReference {






    private astm_Name astm_name;




    private astm_TypeDefinition astm_typedefinition;


    public astm_NamedTypeReference(
    ) {
        super(
        );
    }



    public astm_Name getAstm_name() {
        return astm_name;
    }

    public void setAstm_name(astm_Name astm_name) {
        this.astm_name = astm_name;
    }
    public astm_TypeDefinition getAstm_typedefinition() {
        return astm_typedefinition;
    }

    public void setAstm_typedefinition(astm_TypeDefinition astm_typedefinition) {
        this.astm_typedefinition = astm_typedefinition;
    }

}