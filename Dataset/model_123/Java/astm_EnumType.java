





import java.util.List;
import java.util.ArrayList;

public class astm_EnumType extends DataType {






    private List<astm_EnumLiteralDefinition> astm_enumliteraldefinitions;


    public astm_EnumType(
    ) {
        super(
        );
        this.astm_enumliteraldefinitions = new ArrayList<>();
    }

    public astm_EnumType(
        ArrayList<astm_EnumLiteralDefinition> astm_enumliteraldefinitions    ) {
        this.astm_enumliteraldefinitions = astm_enumliteraldefinitions;
    }


    public List<astm_EnumLiteralDefinition> getAstm_enumliteraldefinitions() {
        return astm_enumliteraldefinitions;
    }

    public void addAstm_enumliteraldefinition(Astm_enumliteraldefinition astm_enumliteraldefinition) {
        this.astm_enumliteraldefinitions.add(astm_enumliteraldefinition);
    }

}