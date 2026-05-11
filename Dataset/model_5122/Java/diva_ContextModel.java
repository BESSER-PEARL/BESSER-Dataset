





import java.util.List;
import java.util.ArrayList;

public class diva_ContextModel extends Visitable {






    private List<diva_VariableValue> diva_variablevalues;


    public diva_ContextModel(
    ) {
        super(
        );
        this.diva_variablevalues = new ArrayList<>();
    }

    public diva_ContextModel(
        ArrayList<diva_VariableValue> diva_variablevalues    ) {
        this.diva_variablevalues = diva_variablevalues;
    }


    public List<diva_VariableValue> getDiva_variablevalues() {
        return diva_variablevalues;
    }

    public void addDiva_variablevalue(Diva_variablevalue diva_variablevalue) {
        this.diva_variablevalues.add(diva_variablevalue);
    }

}