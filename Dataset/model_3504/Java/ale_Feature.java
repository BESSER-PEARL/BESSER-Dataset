





import java.util.List;
import java.util.ArrayList;

public class ale_Feature extends Expression {

    private String feature;





    private ale_Expression ale_expression;


    public ale_Feature(
        String feature    ) {
        super(
        );
        this.feature = feature;
    }


    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }

    public ale_Expression getAle_expression() {
        return ale_expression;
    }

    public void setAle_expression(ale_Expression ale_expression) {
        this.ale_expression = ale_expression;
    }

}