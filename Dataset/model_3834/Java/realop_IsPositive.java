





import java.util.List;
import java.util.ArrayList;

public class realop_IsPositive extends Expression {

    private String featureName;



    public realop_IsPositive(
        String featureName    ) {
        super(
        );
        this.featureName = featureName;
    }


    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }


}