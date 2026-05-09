





import java.util.List;
import java.util.ArrayList;

public class relationpattern_ThingB extends NamedElement, TargetNode {

    private String step;



    public relationpattern_ThingB(
        String step    ) {
        super(
        );
        this.step = step;
    }


    public String getStep() {
        return step;
    }

    public void setStep(String step) {
        this.step = step;
    }


}