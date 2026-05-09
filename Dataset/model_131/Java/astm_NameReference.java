





import java.util.List;
import java.util.ArrayList;

public class astm_NameReference extends Expression {






    private astm_Name astm_name;




    private astm_DefinitionObject astm_definitionobject;


    public astm_NameReference(
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
    public astm_DefinitionObject getAstm_definitionobject() {
        return astm_definitionobject;
    }

    public void setAstm_definitionobject(astm_DefinitionObject astm_definitionobject) {
        this.astm_definitionobject = astm_definitionobject;
    }

}