





import java.util.List;
import java.util.ArrayList;

public class diagraph_DLabeledElement extends DGraphElement {

    private String expression;
    private String labls;





    private List<diagraph_DLabel> diagraph_dlabels;


    public diagraph_DLabeledElement(
        String expression,        String labls    ) {
        super(
        );
        this.expression = expression;
        this.labls = labls;
        this.diagraph_dlabels = new ArrayList<>();
    }

    public diagraph_DLabeledElement(
        String expression,        String labls        ArrayList<diagraph_DLabel> diagraph_dlabels    ) {
        this.expression = expression;
        this.labls = labls;
        this.diagraph_dlabels = diagraph_dlabels;
    }

    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }
    public String getLabls() {
        return labls;
    }

    public void setLabls(String labls) {
        this.labls = labls;
    }

    public List<diagraph_DLabel> getDiagraph_dlabels() {
        return diagraph_dlabels;
    }

    public void addDiagraph_dlabel(Diagraph_dlabel diagraph_dlabel) {
        this.diagraph_dlabels.add(diagraph_dlabel);
    }

}