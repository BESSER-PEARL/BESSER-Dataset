





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedDataType extends TracedClassifier {






    private List<uml_TracedProperty> uml_tracedpropertys;




    private List<uml_TracedOperation> uml_tracedoperations;


    public umlTrace_uml_TracedDataType(
    ) {
        super(
        );
        this.uml_tracedpropertys = new ArrayList<>();
        this.uml_tracedoperations = new ArrayList<>();
    }

    public umlTrace_uml_TracedDataType(
        ArrayList<uml_TracedProperty> uml_tracedpropertys,        ArrayList<uml_TracedOperation> uml_tracedoperations    ) {
        this.uml_tracedpropertys = uml_tracedpropertys;
        this.uml_tracedoperations = uml_tracedoperations;
    }


    public List<uml_TracedProperty> getUml_tracedpropertys() {
        return uml_tracedpropertys;
    }

    public void addUml_tracedproperty(Uml_tracedproperty uml_tracedproperty) {
        this.uml_tracedpropertys.add(uml_tracedproperty);
    }
    public List<uml_TracedOperation> getUml_tracedoperations() {
        return uml_tracedoperations;
    }

    public void addUml_tracedoperation(Uml_tracedoperation uml_tracedoperation) {
        this.uml_tracedoperations.add(uml_tracedoperation);
    }

}