





import java.util.List;
import java.util.ArrayList;

public class uma_Activity extends WorkDefinition, WorkBreakdownElement, VariabilityElement {

    private String isEnactable;



    public uma_Activity(
        String isEnactable    ) {
        super(
        );
        this.isEnactable = isEnactable;
    }


    public String getIsenactable() {
        return isEnactable;
    }

    public void setIsenactable(String isEnactable) {
        this.isEnactable = isEnactable;
    }


}