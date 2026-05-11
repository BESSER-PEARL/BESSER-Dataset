





import java.util.List;
import java.util.ArrayList;

public class iec61131_sfc_Steps2 extends Steps {






    private List<Step_Name> step_names;


    public iec61131_sfc_Steps2(
    ) {
        super(
        );
        this.step_names = new ArrayList<>();
    }

    public iec61131_sfc_Steps2(
        ArrayList<Step_Name> step_names    ) {
        this.step_names = step_names;
    }


    public List<Step_Name> getStep_names() {
        return step_names;
    }

    public void addStep_name(Step_name step_name) {
        this.step_names.add(step_name);
    }

}