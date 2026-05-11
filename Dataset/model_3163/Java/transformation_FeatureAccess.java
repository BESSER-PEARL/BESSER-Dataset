





import java.util.List;
import java.util.ArrayList;

public class transformation_FeatureAccess extends Expression {

    private boolean spreading;
    private boolean nullable;





    private transformation_Expression transformation_expression;


    public transformation_FeatureAccess(
        boolean spreading,        boolean nullable    ) {
        super(
        );
        this.spreading = spreading;
        this.nullable = nullable;
    }


    public boolean getSpreading() {
        return spreading;
    }

    public void setSpreading(boolean spreading) {
        this.spreading = spreading;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }

    public transformation_Expression getTransformation_expression() {
        return transformation_expression;
    }

    public void setTransformation_expression(transformation_Expression transformation_expression) {
        this.transformation_expression = transformation_expression;
    }

}