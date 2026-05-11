





import java.util.List;
import java.util.ArrayList;

public class UML2_Property  {

    private String aggregation;





    private UML2_Association uml2_association;


    public UML2_Property(
        String aggregation    ) {
        this.aggregation = aggregation;
    }


    public String getAggregation() {
        return aggregation;
    }

    public void setAggregation(String aggregation) {
        this.aggregation = aggregation;
    }

    public UML2_Association getUml2_association() {
        return uml2_association;
    }

    public void setUml2_association(UML2_Association uml2_association) {
        this.uml2_association = uml2_association;
    }

}