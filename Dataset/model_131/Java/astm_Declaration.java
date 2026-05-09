





import java.util.List;
import java.util.ArrayList;

public class astm_Declaration extends DeclarationOrDefinition {






    private astm_Definition astm_definition;




    private astm_Name astm_name;


    public astm_Declaration(
    ) {
        super(
        );
    }



    public astm_Definition getAstm_definition() {
        return astm_definition;
    }

    public void setAstm_definition(astm_Definition astm_definition) {
        this.astm_definition = astm_definition;
    }
    public astm_Name getAstm_name() {
        return astm_name;
    }

    public void setAstm_name(astm_Name astm_name) {
        this.astm_name = astm_name;
    }

}