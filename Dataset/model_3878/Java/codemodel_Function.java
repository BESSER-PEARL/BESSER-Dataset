





import java.util.List;
import java.util.ArrayList;

public class codemodel_Function extends CMElement {

    private String identifier;





    private codemodel_CodeModule codemodel_codemodule;


    public codemodel_Function(
        String identifier    ) {
        super(
        );
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public codemodel_CodeModule getCodemodel_codemodule() {
        return codemodel_codemodule;
    }

    public void setCodemodel_codemodule(codemodel_CodeModule codemodel_codemodule) {
        this.codemodel_codemodule = codemodel_codemodule;
    }

}