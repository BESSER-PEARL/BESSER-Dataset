





import java.util.List;
import java.util.ArrayList;

public class graph_Label extends Identifiable {

    private String uRIOfIdentifiableToBeLabeled;





    private graph_LabelValue graph_labelvalue;


    public graph_Label(
        String uRIOfIdentifiableToBeLabeled    ) {
        super(
        );
        this.uRIOfIdentifiableToBeLabeled = uRIOfIdentifiableToBeLabeled;
    }


    public String getUriofidentifiabletobelabeled() {
        return uRIOfIdentifiableToBeLabeled;
    }

    public void setUriofidentifiabletobelabeled(String uRIOfIdentifiableToBeLabeled) {
        this.uRIOfIdentifiableToBeLabeled = uRIOfIdentifiableToBeLabeled;
    }

    public graph_LabelValue getGraph_labelvalue() {
        return graph_labelvalue;
    }

    public void setGraph_labelvalue(graph_LabelValue graph_labelvalue) {
        this.graph_labelvalue = graph_labelvalue;
    }

}