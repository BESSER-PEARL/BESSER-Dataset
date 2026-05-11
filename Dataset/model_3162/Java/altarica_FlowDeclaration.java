





import java.util.List;
import java.util.ArrayList;

public class altarica_FlowDeclaration  {

    private String kind;





    private altarica_VariableAttribute altarica_variableattribute;




    private List<altarica_Flow> altarica_flows;




    private altarica_FlowSpecification altarica_flowspecification;


    public altarica_FlowDeclaration(
        String kind    ) {
        this.kind = kind;
        this.altarica_flows = new ArrayList<>();
    }

    public altarica_FlowDeclaration(
        String kind        ArrayList<altarica_Flow> altarica_flows    ) {
        this.kind = kind;
        this.altarica_flows = altarica_flows;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public altarica_VariableAttribute getAltarica_variableattribute() {
        return altarica_variableattribute;
    }

    public void setAltarica_variableattribute(altarica_VariableAttribute altarica_variableattribute) {
        this.altarica_variableattribute = altarica_variableattribute;
    }
    public List<altarica_Flow> getAltarica_flows() {
        return altarica_flows;
    }

    public void addAltarica_flow(Altarica_flow altarica_flow) {
        this.altarica_flows.add(altarica_flow);
    }
    public altarica_FlowSpecification getAltarica_flowspecification() {
        return altarica_flowspecification;
    }

    public void setAltarica_flowspecification(altarica_FlowSpecification altarica_flowspecification) {
        this.altarica_flowspecification = altarica_flowspecification;
    }

}