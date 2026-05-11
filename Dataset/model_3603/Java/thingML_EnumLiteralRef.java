





import java.util.List;
import java.util.ArrayList;

public class thingML_EnumLiteralRef extends Expression {






    private thingML_Enumeration thingml_enumeration;




    private thingML_EnumerationLiteral thingml_enumerationliteral;


    public thingML_EnumLiteralRef(
    ) {
        super(
        );
    }



    public thingML_Enumeration getThingml_enumeration() {
        return thingml_enumeration;
    }

    public void setThingml_enumeration(thingML_Enumeration thingml_enumeration) {
        this.thingml_enumeration = thingml_enumeration;
    }
    public thingML_EnumerationLiteral getThingml_enumerationliteral() {
        return thingml_enumerationliteral;
    }

    public void setThingml_enumerationliteral(thingML_EnumerationLiteral thingml_enumerationliteral) {
        this.thingml_enumerationliteral = thingml_enumerationliteral;
    }

}