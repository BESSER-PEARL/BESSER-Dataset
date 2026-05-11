





import java.util.List;
import java.util.ArrayList;

public class diva_Scenario extends NamedElement {






    private List<diva_Context> diva_contexts;


    public diva_Scenario(
    ) {
        super(
        );
        this.diva_contexts = new ArrayList<>();
    }

    public diva_Scenario(
        ArrayList<diva_Context> diva_contexts    ) {
        this.diva_contexts = diva_contexts;
    }


    public List<diva_Context> getDiva_contexts() {
        return diva_contexts;
    }

    public void addDiva_context(Diva_context diva_context) {
        this.diva_contexts.add(diva_context);
    }

}