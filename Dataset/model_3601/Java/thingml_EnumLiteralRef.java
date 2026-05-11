





import java.util.List;
import java.util.ArrayList;

public class thingml_EnumLiteralRef extends Literal {






    private thingml_Enumeration thingml_enumeration;




    private thingml_EnumerationLiteral thingml_enumerationliteral;


    public thingml_EnumLiteralRef(
    ) {
        super(
        );
    }



    public thingml_Enumeration getThingml_enumeration() {
        return thingml_enumeration;
    }

    public void setThingml_enumeration(thingml_Enumeration thingml_enumeration) {
        this.thingml_enumeration = thingml_enumeration;
    }
    public thingml_EnumerationLiteral getThingml_enumerationliteral() {
        return thingml_enumerationliteral;
    }

    public void setThingml_enumerationliteral(thingml_EnumerationLiteral thingml_enumerationliteral) {
        this.thingml_enumerationliteral = thingml_enumerationliteral;
    }

}