





import java.util.List;
import java.util.ArrayList;

public class UML2_Property  {

    private boolean isComposite;
    private String aggregation;



    public UML2_Property(
        boolean isComposite,        String aggregation    ) {
        this.isComposite = isComposite;
        this.aggregation = aggregation;
    }


    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }
    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }


}