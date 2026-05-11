





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedSignal extends TracedClassifier {






    private List<uml_TracedProperty> uml_tracedpropertys;


    public umlTrace_uml_TracedSignal(
    ) {
        super(
        );
        this.uml_tracedpropertys = new ArrayList<>();
    }

    public umlTrace_uml_TracedSignal(
        ArrayList<uml_TracedProperty> uml_tracedpropertys    ) {
        this.uml_tracedpropertys = uml_tracedpropertys;
    }


    public List<uml_TracedProperty> getUml_tracedpropertys() {
        return uml_tracedpropertys;
    }

    public void addUml_tracedproperty(Uml_tracedproperty uml_tracedproperty) {
        this.uml_tracedpropertys.add(uml_tracedproperty);
    }

}