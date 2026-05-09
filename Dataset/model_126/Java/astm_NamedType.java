





import java.util.List;
import java.util.ArrayList;

public class astm_NamedType extends DataType {






    private astm_DerivesFrom astm_derivesfrom;




    private astm_NamedTypeDefinition astm_namedtypedefinition;




    private astm_Type astm_type;


    public astm_NamedType(
    ) {
        super(
        );
    }



    public astm_DerivesFrom getAstm_derivesfrom() {
        return astm_derivesfrom;
    }

    public void setAstm_derivesfrom(astm_DerivesFrom astm_derivesfrom) {
        this.astm_derivesfrom = astm_derivesfrom;
    }
    public astm_NamedTypeDefinition getAstm_namedtypedefinition() {
        return astm_namedtypedefinition;
    }

    public void setAstm_namedtypedefinition(astm_NamedTypeDefinition astm_namedtypedefinition) {
        this.astm_namedtypedefinition = astm_namedtypedefinition;
    }
    public astm_Type getAstm_type() {
        return astm_type;
    }

    public void setAstm_type(astm_Type astm_type) {
        this.astm_type = astm_type;
    }

}