





import java.util.List;
import java.util.ArrayList;

public class urml_SendTrigger extends StatementOperation, Statement {






    private List<urml_Trigger_out> urml_trigger_outs;


    public urml_SendTrigger(
    ) {
        super(
        );
        this.urml_trigger_outs = new ArrayList<>();
    }

    public urml_SendTrigger(
        ArrayList<urml_Trigger_out> urml_trigger_outs    ) {
        this.urml_trigger_outs = urml_trigger_outs;
    }


    public List<urml_Trigger_out> getUrml_trigger_outs() {
        return urml_trigger_outs;
    }

    public void addUrml_trigger_out(Urml_trigger_out urml_trigger_out) {
        this.urml_trigger_outs.add(urml_trigger_out);
    }

}