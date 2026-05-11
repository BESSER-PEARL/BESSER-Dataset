





import java.util.List;
import java.util.ArrayList;

public class sooml_Class extends NamedElement {






    private sooml_StateMachine sooml_statemachine;




    private sooml_StateMachine sooml_statemachine;




    private List<sooml_Operation> sooml_operations;




    private sooml_Package sooml_package;


    public sooml_Class(
    ) {
        super(
        );
        this.sooml_operations = new ArrayList<>();
    }

    public sooml_Class(
        ArrayList<sooml_Operation> sooml_operations    ) {
        this.sooml_operations = sooml_operations;
    }


    public sooml_StateMachine getSooml_statemachine() {
        return sooml_statemachine;
    }

    public void setSooml_statemachine(sooml_StateMachine sooml_statemachine) {
        this.sooml_statemachine = sooml_statemachine;
    }
    public sooml_StateMachine getSooml_statemachine() {
        return sooml_statemachine;
    }

    public void setSooml_statemachine(sooml_StateMachine sooml_statemachine) {
        this.sooml_statemachine = sooml_statemachine;
    }
    public List<sooml_Operation> getSooml_operations() {
        return sooml_operations;
    }

    public void addSooml_operation(Sooml_operation sooml_operation) {
        this.sooml_operations.add(sooml_operation);
    }
    public sooml_Package getSooml_package() {
        return sooml_package;
    }

    public void setSooml_package(sooml_Package sooml_package) {
        this.sooml_package = sooml_package;
    }

}