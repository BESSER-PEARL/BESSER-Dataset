





import java.util.List;
import java.util.ArrayList;

public class cpsml_State  {

    private boolean name;





    private List<cpsml_Variable> cpsml_variables;




    private cpsml_System cpsml_system;




    private cpsml_System cpsml_system;




    private cpsml_System cpsml_system;




    private List<cpsml_State> cpsml_states;




    private cpsml_Variable cpsml_variable;




    private cpsml_System cpsml_system;




    private cpsml_State cpsml_state;


    public cpsml_State(
        boolean name    ) {
        this.name = name;
        this.cpsml_variables = new ArrayList<>();
        this.cpsml_states = new ArrayList<>();
    }

    public cpsml_State(
        boolean name        ArrayList<cpsml_Variable> cpsml_variables,        ArrayList<cpsml_State> cpsml_states    ) {
        this.name = name;
        this.cpsml_variables = cpsml_variables;
        this.cpsml_states = cpsml_states;
    }

    public boolean getName() {
        return name;
    }

    public void setName(boolean name) {
        this.name = name;
    }

    public List<cpsml_Variable> getCpsml_variables() {
        return cpsml_variables;
    }

    public void addCpsml_variable(Cpsml_variable cpsml_variable) {
        this.cpsml_variables.add(cpsml_variable);
    }
    public cpsml_System getCpsml_system() {
        return cpsml_system;
    }

    public void setCpsml_system(cpsml_System cpsml_system) {
        this.cpsml_system = cpsml_system;
    }
    public cpsml_System getCpsml_system() {
        return cpsml_system;
    }

    public void setCpsml_system(cpsml_System cpsml_system) {
        this.cpsml_system = cpsml_system;
    }
    public cpsml_System getCpsml_system() {
        return cpsml_system;
    }

    public void setCpsml_system(cpsml_System cpsml_system) {
        this.cpsml_system = cpsml_system;
    }
    public List<cpsml_State> getCpsml_states() {
        return cpsml_states;
    }

    public void addCpsml_state(Cpsml_state cpsml_state) {
        this.cpsml_states.add(cpsml_state);
    }
    public cpsml_Variable getCpsml_variable() {
        return cpsml_variable;
    }

    public void setCpsml_variable(cpsml_Variable cpsml_variable) {
        this.cpsml_variable = cpsml_variable;
    }
    public cpsml_System getCpsml_system() {
        return cpsml_system;
    }

    public void setCpsml_system(cpsml_System cpsml_system) {
        this.cpsml_system = cpsml_system;
    }
    public cpsml_State getCpsml_state() {
        return cpsml_state;
    }

    public void setCpsml_state(cpsml_State cpsml_state) {
        this.cpsml_state = cpsml_state;
    }

}