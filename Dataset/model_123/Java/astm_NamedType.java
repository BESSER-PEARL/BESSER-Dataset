





import java.util.List;
import java.util.ArrayList;

public class astm_NamedType extends DataType {






    private astm_NamedTypeDefinition astm_namedtypedefinition;




    private astm_DerivesFrom astm_derivesfrom;


    public astm_NamedType(
    ) {
        super(
        );
    }



    public astm_NamedTypeDefinition getAstm_namedtypedefinition() {
        return astm_namedtypedefinition;
    }

    public void setAstm_namedtypedefinition(astm_NamedTypeDefinition astm_namedtypedefinition) {
        this.astm_namedtypedefinition = astm_namedtypedefinition;
    }
    public astm_DerivesFrom getAstm_derivesfrom() {
        return astm_derivesfrom;
    }

    public void setAstm_derivesfrom(astm_DerivesFrom astm_derivesfrom) {
        this.astm_derivesfrom = astm_derivesfrom;
    }

}