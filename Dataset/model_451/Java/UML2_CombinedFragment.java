





import java.util.List;
import java.util.ArrayList;

public class UML2_CombinedFragment extends InteractionFragment {

    private String interactionOperator;



    public UML2_CombinedFragment(
        String interactionOperator    ) {
        super(
        );
        this.interactionOperator = interactionOperator;
    }


    public String getInteractionoperator() {
        return interactionOperator;
    }

    public void setInteractionoperator(String interactionOperator) {
        this.interactionOperator = interactionOperator;
    }


}