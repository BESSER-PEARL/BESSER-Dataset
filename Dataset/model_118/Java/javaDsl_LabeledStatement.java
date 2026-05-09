





import java.util.List;
import java.util.ArrayList;

public class javaDsl_LabeledStatement extends Statement {

    private String label;



    public javaDsl_LabeledStatement(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}