





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Property extends Element {

    private String aggregation;



    public UML2WithID_Property(
        String aggregation    ) {
        super(
        );
        this.aggregation = aggregation;
    }


    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }


}