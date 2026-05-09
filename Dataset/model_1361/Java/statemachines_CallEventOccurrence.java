





import java.util.List;
import java.util.ArrayList;

public class statemachines_CallEventOccurrence extends EventOccurrence {






    private List<statemachines_AttributeValue> statemachines_attributevalues;




    private statemachines_Operation statemachines_operation;




    private List<statemachines_AttributeValue> statemachines_attributevalues;




    private statemachines_AttributeValue statemachines_attributevalue;


    public statemachines_CallEventOccurrence(
    ) {
        super(
        );
        this.statemachines_attributevalues = new ArrayList<>();
        this.statemachines_attributevalues = new ArrayList<>();
    }

    public statemachines_CallEventOccurrence(
        ArrayList<statemachines_AttributeValue> statemachines_attributevalues,        ArrayList<statemachines_AttributeValue> statemachines_attributevalues    ) {
        this.statemachines_attributevalues = statemachines_attributevalues;
        this.statemachines_attributevalues = statemachines_attributevalues;
    }


    public List<statemachines_AttributeValue> getStatemachines_attributevalues() {
        return statemachines_attributevalues;
    }

    public void addStatemachines_attributevalue(Statemachines_attributevalue statemachines_attributevalue) {
        this.statemachines_attributevalues.add(statemachines_attributevalue);
    }
    public statemachines_Operation getStatemachines_operation() {
        return statemachines_operation;
    }

    public void setStatemachines_operation(statemachines_Operation statemachines_operation) {
        this.statemachines_operation = statemachines_operation;
    }
    public List<statemachines_AttributeValue> getStatemachines_attributevalues() {
        return statemachines_attributevalues;
    }

    public void addStatemachines_attributevalue(Statemachines_attributevalue statemachines_attributevalue) {
        this.statemachines_attributevalues.add(statemachines_attributevalue);
    }
    public statemachines_AttributeValue getStatemachines_attributevalue() {
        return statemachines_attributevalue;
    }

    public void setStatemachines_attributevalue(statemachines_AttributeValue statemachines_attributevalue) {
        this.statemachines_attributevalue = statemachines_attributevalue;
    }

}