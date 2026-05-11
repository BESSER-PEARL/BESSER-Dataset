





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_Reference2Reference extends Feature2Feature {

    private String cardinality;
    private String resolverName;



    public frontend_mappings_Reference2Reference(
        String cardinality,        String resolverName    ) {
        super(
        );
        this.cardinality = cardinality;
        this.resolverName = resolverName;
    }


    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }
    public String getResolvername() {
        return resolverName;
    }

    public void setResolvername(String resolverName) {
        this.resolverName = resolverName;
    }


}