





import java.util.List;
import java.util.ArrayList;

public class table_DCell extends DSemanticDecorator, DTableElement {

    private String label;



    public table_DCell(
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