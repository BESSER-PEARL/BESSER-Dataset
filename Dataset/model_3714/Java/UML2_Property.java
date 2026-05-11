





import java.util.List;
import java.util.ArrayList;

public class UML2_Property  {

    private String aggregation;
    private boolean isComposite;



    public UML2_Property(
        String aggregation,        boolean isComposite    ) {
        this.aggregation = aggregation;
        this.isComposite = isComposite;
    }


    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }
    public boolean getIscomposite() {
        return isComposite;
    }

    public void setIscomposite(boolean isComposite) {
        this.isComposite = isComposite;
    }


}