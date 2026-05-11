





import java.util.List;
import java.util.ArrayList;

public class trnetvisual_AttributePattern extends Parameter {

    private String name;
    private float expectedNumberOfDistinctValues;



    public trnetvisual_AttributePattern(
        String name,        float expectedNumberOfDistinctValues    ) {
        super(
        );
        this.name = name;
        this.expectedNumberOfDistinctValues = expectedNumberOfDistinctValues;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getExpectednumberofdistinctvalues() {
        return expectedNumberOfDistinctValues;
    }

    public void setExpectednumberofdistinctvalues(float expectedNumberOfDistinctValues) {
        this.expectedNumberOfDistinctValues = expectedNumberOfDistinctValues;
    }


}