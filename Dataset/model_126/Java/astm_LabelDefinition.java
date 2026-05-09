





import java.util.List;
import java.util.ArrayList;

public class astm_LabelDefinition extends DefinitionObject {






    private astm_Name astm_name;




    private astm_LabelType astm_labeltype;


    public astm_LabelDefinition(
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
    public astm_LabelType getAstm_labeltype() {
        return astm_labeltype;
    }

    public void setAstm_labeltype(astm_LabelType astm_labeltype) {
        this.astm_labeltype = astm_labeltype;
    }

}