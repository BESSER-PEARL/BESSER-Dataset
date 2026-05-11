





import java.util.List;
import java.util.ArrayList;

public class xpand3_declaration_Check extends AbstractDeclaration {

    private boolean errorSeverity;
    private String feature;



    public xpand3_declaration_Check(
        boolean errorSeverity,        String feature    ) {
        super(
        );
        this.errorSeverity = errorSeverity;
        this.feature = feature;
    }


    public boolean getErrorseverity() {
        return errorSeverity;
    }

    public void setErrorseverity(boolean errorSeverity) {
        this.errorSeverity = errorSeverity;
    }
    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }


}