





import java.util.List;
import java.util.ArrayList;

public class form_FormButton extends Widget {

    private String labelBehavior;



    public form_FormButton(
        String labelBehavior    ) {
        super(
        );
        this.labelBehavior = labelBehavior;
    }


    public String getLabelbehavior() {
        return labelBehavior;
    }

    public void setLabelbehavior(String labelBehavior) {
        this.labelBehavior = labelBehavior;
    }


}