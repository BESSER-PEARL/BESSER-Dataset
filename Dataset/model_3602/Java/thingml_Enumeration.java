





import java.util.List;
import java.util.ArrayList;

public class thingml_Enumeration extends Type {






    private thingml_EnumerationLiteral thingml_enumerationliteral;




    private List<thingml_EnumerationLiteral> thingml_enumerationliterals;


    public thingml_Enumeration(
    ) {
        super(
        );
        this.thingml_enumerationliterals = new ArrayList<>();
    }

    public thingml_Enumeration(
        ArrayList<thingml_EnumerationLiteral> thingml_enumerationliterals    ) {
        this.thingml_enumerationliterals = thingml_enumerationliterals;
    }


    public thingml_EnumerationLiteral getThingml_enumerationliteral() {
        return thingml_enumerationliteral;
    }

    public void setThingml_enumerationliteral(thingml_EnumerationLiteral thingml_enumerationliteral) {
        this.thingml_enumerationliteral = thingml_enumerationliteral;
    }
    public List<thingml_EnumerationLiteral> getThingml_enumerationliterals() {
        return thingml_enumerationliterals;
    }

    public void addThingml_enumerationliteral(Thingml_enumerationliteral thingml_enumerationliteral) {
        this.thingml_enumerationliterals.add(thingml_enumerationliteral);
    }

}