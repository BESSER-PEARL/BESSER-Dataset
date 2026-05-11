





import java.util.List;
import java.util.ArrayList;

public class Maude_Parameter extends ModExpression {

    private String label;



    public Maude_Parameter(
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