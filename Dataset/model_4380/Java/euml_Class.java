





import java.util.List;
import java.util.ArrayList;

public class euml_Class extends NamedElement {






    private List<euml_Realization> euml_realizations;




    private List<euml_Operation> euml_operations;




    private List<euml_Generalization> euml_generalizations;




    private euml_Operation euml_operation;




    private List<euml_Dependecy> euml_dependecys;




    private euml_Package euml_package;


    public euml_Class(
    ) {
        super(
        );
        this.euml_realizations = new ArrayList<>();
        this.euml_operations = new ArrayList<>();
        this.euml_generalizations = new ArrayList<>();
        this.euml_dependecys = new ArrayList<>();
    }

    public euml_Class(
        ArrayList<euml_Realization> euml_realizations,        ArrayList<euml_Operation> euml_operations,        ArrayList<euml_Generalization> euml_generalizations,        ArrayList<euml_Dependecy> euml_dependecys    ) {
        this.euml_realizations = euml_realizations;
        this.euml_operations = euml_operations;
        this.euml_generalizations = euml_generalizations;
        this.euml_dependecys = euml_dependecys;
    }


    public List<euml_Realization> getEuml_realizations() {
        return euml_realizations;
    }

    public void addEuml_realization(Euml_realization euml_realization) {
        this.euml_realizations.add(euml_realization);
    }
    public List<euml_Operation> getEuml_operations() {
        return euml_operations;
    }

    public void addEuml_operation(Euml_operation euml_operation) {
        this.euml_operations.add(euml_operation);
    }
    public List<euml_Generalization> getEuml_generalizations() {
        return euml_generalizations;
    }

    public void addEuml_generalization(Euml_generalization euml_generalization) {
        this.euml_generalizations.add(euml_generalization);
    }
    public euml_Operation getEuml_operation() {
        return euml_operation;
    }

    public void setEuml_operation(euml_Operation euml_operation) {
        this.euml_operation = euml_operation;
    }
    public List<euml_Dependecy> getEuml_dependecys() {
        return euml_dependecys;
    }

    public void addEuml_dependecy(Euml_dependecy euml_dependecy) {
        this.euml_dependecys.add(euml_dependecy);
    }
    public euml_Package getEuml_package() {
        return euml_package;
    }

    public void setEuml_package(euml_Package euml_package) {
        this.euml_package = euml_package;
    }

}