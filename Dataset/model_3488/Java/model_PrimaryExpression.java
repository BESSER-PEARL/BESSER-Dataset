





import java.util.List;
import java.util.ArrayList;

public class model_PrimaryExpression extends Expression {

    private String featureId;



    public model_PrimaryExpression(
        String featureId    ) {
        super(
        );
        this.featureId = featureId;
    }


    public String getFeatureid() {
        return featureId;
    }

    public void setFeatureid(String featureId) {
        this.featureId = featureId;
    }


}