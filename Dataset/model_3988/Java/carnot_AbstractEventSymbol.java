





import java.util.List;
import java.util.ArrayList;

public class carnot_AbstractEventSymbol extends IFlowObjectSymbol, IModelElementNodeSymbol {

    private String label;



    public carnot_AbstractEventSymbol(
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