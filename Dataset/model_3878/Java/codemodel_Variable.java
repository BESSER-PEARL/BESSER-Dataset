





import java.util.List;
import java.util.ArrayList;

public class codemodel_Variable extends CMElement {

    private String identifier;
    private boolean constant;





    private codemodel_DataType codemodel_datatype;


    public codemodel_Variable(
        String identifier,        boolean constant    ) {
        super(
        );
        this.identifier = identifier;
        this.constant = constant;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }

    public codemodel_DataType getCodemodel_datatype() {
        return codemodel_datatype;
    }

    public void setCodemodel_datatype(codemodel_DataType codemodel_datatype) {
        this.codemodel_datatype = codemodel_datatype;
    }

}