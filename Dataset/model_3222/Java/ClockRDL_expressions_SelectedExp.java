





import java.util.List;
import java.util.ArrayList;

public class ClockRDL_expressions_SelectedExp extends PrefixedExp {

    private String selector;



    public ClockRDL_expressions_SelectedExp(
        String selector    ) {
        super(
        );
        this.selector = selector;
    }


    public String getSelector() {
        return selector;
    }

    public void setSelector(String selector) {
        this.selector = selector;
    }


}