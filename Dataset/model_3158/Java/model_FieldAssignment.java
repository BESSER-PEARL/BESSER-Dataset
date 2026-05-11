





import java.util.List;
import java.util.ArrayList;

public class model_FieldAssignment  {

    private String reference;





    private model_RecordLiteralExpression model_recordliteralexpression;


    public model_FieldAssignment(
        String reference    ) {
        this.reference = reference;
    }


    public String getReference() {
        return reference;
    }

    public void setReference(String reference) {
        this.reference = reference;
    }

    public model_RecordLiteralExpression getModel_recordliteralexpression() {
        return model_recordliteralexpression;
    }

    public void setModel_recordliteralexpression(model_RecordLiteralExpression model_recordliteralexpression) {
        this.model_recordliteralexpression = model_recordliteralexpression;
    }

}