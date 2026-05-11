





import java.util.List;
import java.util.ArrayList;

public class oogen_OOFieldReferenceExpression extends OOExpression {

    private String fieldName;





    private oogen_OOExpression oogen_ooexpression;


    public oogen_OOFieldReferenceExpression(
        String fieldName    ) {
        super(
        );
        this.fieldName = fieldName;
    }


    public String getFieldname() {
        return fieldName;
    }

    public void setFieldname(String fieldName) {
        this.fieldName = fieldName;
    }

    public oogen_OOExpression getOogen_ooexpression() {
        return oogen_ooexpression;
    }

    public void setOogen_ooexpression(oogen_OOExpression oogen_ooexpression) {
        this.oogen_ooexpression = oogen_ooexpression;
    }

}