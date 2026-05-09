





import java.util.List;
import java.util.ArrayList;

public class trace_Traced_TracedObjects  {






    private List<model2_TracedA> model2_tracedas;




    private List<model2Configuration_TracedC> model2configuration_tracedcs;




    private List<model2Configuration_TracedB> model2configuration_tracedbs;


    public trace_Traced_TracedObjects(
    ) {
        this.model2_tracedas = new ArrayList<>();
        this.model2configuration_tracedcs = new ArrayList<>();
        this.model2configuration_tracedbs = new ArrayList<>();
    }

    public trace_Traced_TracedObjects(
        ArrayList<model2_TracedA> model2_tracedas,        ArrayList<model2Configuration_TracedC> model2configuration_tracedcs,        ArrayList<model2Configuration_TracedB> model2configuration_tracedbs    ) {
        this.model2_tracedas = model2_tracedas;
        this.model2configuration_tracedcs = model2configuration_tracedcs;
        this.model2configuration_tracedbs = model2configuration_tracedbs;
    }


    public List<model2_TracedA> getModel2_tracedas() {
        return model2_tracedas;
    }

    public void addModel2_traceda(Model2_traceda model2_traceda) {
        this.model2_tracedas.add(model2_traceda);
    }
    public List<model2Configuration_TracedC> getModel2configuration_tracedcs() {
        return model2configuration_tracedcs;
    }

    public void addModel2configuration_tracedc(Model2configuration_tracedc model2configuration_tracedc) {
        this.model2configuration_tracedcs.add(model2configuration_tracedc);
    }
    public List<model2Configuration_TracedB> getModel2configuration_tracedbs() {
        return model2configuration_tracedbs;
    }

    public void addModel2configuration_tracedb(Model2configuration_tracedb model2configuration_tracedb) {
        this.model2configuration_tracedbs.add(model2configuration_tracedb);
    }

}