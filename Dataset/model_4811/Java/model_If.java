





import java.util.List;
import java.util.ArrayList;

public class model_If extends Activity {






    private model_Activity model_activity;




    private List<model_ElseIf> model_elseifs;




    private model_Else model_else;


    public model_If(
    ) {
        super(
        );
        this.model_elseifs = new ArrayList<>();
    }

    public model_If(
        ArrayList<model_ElseIf> model_elseifs    ) {
        this.model_elseifs = model_elseifs;
    }


    public model_Activity getModel_activity() {
        return model_activity;
    }

    public void setModel_activity(model_Activity model_activity) {
        this.model_activity = model_activity;
    }
    public List<model_ElseIf> getModel_elseifs() {
        return model_elseifs;
    }

    public void addModel_elseif(Model_elseif model_elseif) {
        this.model_elseifs.add(model_elseif);
    }
    public model_Else getModel_else() {
        return model_else;
    }

    public void setModel_else(model_Else model_else) {
        this.model_else = model_else;
    }

}