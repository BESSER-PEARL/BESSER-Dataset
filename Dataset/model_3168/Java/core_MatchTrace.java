





import java.util.List;
import java.util.ArrayList;

public class core_MatchTrace extends Expression {

    private String cardinality;



    public core_MatchTrace(
        String cardinality    ) {
        super(
        );
        this.cardinality = cardinality;
    }


    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }


}