





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Reception extends BehavioralFeature {

    private String signal;





    private UMLModel_Class umlmodel_class;




    private UMLModel_Interface umlmodel_interface;


    public UMLModel_Reception(
        String signal    ) {
        super(
        );
        this.signal = signal;
    }


    public String getSignal() {
        return signal;
    }

    public void setSignal(String signal) {
        this.signal = signal;
    }

    public UMLModel_Class getUmlmodel_class() {
        return umlmodel_class;
    }

    public void setUmlmodel_class(UMLModel_Class umlmodel_class) {
        this.umlmodel_class = umlmodel_class;
    }
    public UMLModel_Interface getUmlmodel_interface() {
        return umlmodel_interface;
    }

    public void setUmlmodel_interface(UMLModel_Interface umlmodel_interface) {
        this.umlmodel_interface = umlmodel_interface;
    }

}