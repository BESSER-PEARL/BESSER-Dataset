





import java.util.List;
import java.util.ArrayList;

public class altarica_StateDeclaration  {






    private altarica_StateSpecification altarica_statespecification;




    private List<altarica_State> altarica_states;




    private altarica_VariableAttribute altarica_variableattribute;




    private altarica_AbstractTypeRef altarica_abstracttyperef;


    public altarica_StateDeclaration(
    ) {
        this.altarica_states = new ArrayList<>();
    }

    public altarica_StateDeclaration(
        ArrayList<altarica_State> altarica_states    ) {
        this.altarica_states = altarica_states;
    }


    public altarica_StateSpecification getAltarica_statespecification() {
        return altarica_statespecification;
    }

    public void setAltarica_statespecification(altarica_StateSpecification altarica_statespecification) {
        this.altarica_statespecification = altarica_statespecification;
    }
    public List<altarica_State> getAltarica_states() {
        return altarica_states;
    }

    public void addAltarica_state(Altarica_state altarica_state) {
        this.altarica_states.add(altarica_state);
    }
    public altarica_VariableAttribute getAltarica_variableattribute() {
        return altarica_variableattribute;
    }

    public void setAltarica_variableattribute(altarica_VariableAttribute altarica_variableattribute) {
        this.altarica_variableattribute = altarica_variableattribute;
    }
    public altarica_AbstractTypeRef getAltarica_abstracttyperef() {
        return altarica_abstracttyperef;
    }

    public void setAltarica_abstracttyperef(altarica_AbstractTypeRef altarica_abstracttyperef) {
        this.altarica_abstracttyperef = altarica_abstracttyperef;
    }

}