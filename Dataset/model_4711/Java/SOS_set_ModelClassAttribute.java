





import java.util.List;
import java.util.ArrayList;

public class SOS_set_ModelClassAttribute extends Term {

    private String attributeName;





    private VariableRef variableref;


    public SOS_set_ModelClassAttribute(
        String attributeName    ) {
        super(
        );
        this.attributeName = attributeName;
    }


    public String getAttributename() {
        return attributeName;
    }

    public void setAttributename(String attributeName) {
        this.attributeName = attributeName;
    }

    public VariableRef getVariableref() {
        return variableref;
    }

    public void setVariableref(VariableRef variableref) {
        this.variableref = variableref;
    }

}