





import java.util.List;
import java.util.ArrayList;

public class codemodel_DataType extends CMElement {

    private String basetype;





    private codemodel_CodeModule codemodel_codemodule;


    public codemodel_DataType(
        String basetype    ) {
        super(
        );
        this.basetype = basetype;
    }


    public String getBasetype() {
        return basetype;
    }

    public void setBasetype(String basetype) {
        this.basetype = basetype;
    }

    public codemodel_CodeModule getCodemodel_codemodule() {
        return codemodel_codemodule;
    }

    public void setCodemodel_codemodule(codemodel_CodeModule codemodel_codemodule) {
        this.codemodel_codemodule = codemodel_codemodule;
    }

}