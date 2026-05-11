





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_ConfigConstraint extends Constraint {

    private String kind;



    public FeatureModel_ConfigConstraint(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }


}