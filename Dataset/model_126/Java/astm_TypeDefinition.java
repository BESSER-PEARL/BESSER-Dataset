





import java.util.List;
import java.util.ArrayList;

public class astm_TypeDefinition extends DefinitionObject {






    private astm_Name astm_name;




    private astm_NamedTypeReference astm_namedtypereference;


    public astm_TypeDefinition(
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
    public astm_NamedTypeReference getAstm_namedtypereference() {
        return astm_namedtypereference;
    }

    public void setAstm_namedtypereference(astm_NamedTypeReference astm_namedtypereference) {
        this.astm_namedtypereference = astm_namedtypereference;
    }

}