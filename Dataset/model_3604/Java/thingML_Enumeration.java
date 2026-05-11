





import java.util.List;
import java.util.ArrayList;

public class thingML_Enumeration extends Type {






    private List<thingML_EnumerationLiteral> thingml_enumerationliterals;




    private thingML_TypeRef thingml_typeref;


    public thingML_Enumeration(
    ) {
        super(
        );
        this.thingml_enumerationliterals = new ArrayList<>();
    }

    public thingML_Enumeration(
        ArrayList<thingML_EnumerationLiteral> thingml_enumerationliterals    ) {
        this.thingml_enumerationliterals = thingml_enumerationliterals;
    }


    public List<thingML_EnumerationLiteral> getThingml_enumerationliterals() {
        return thingml_enumerationliterals;
    }

    public void addThingml_enumerationliteral(Thingml_enumerationliteral thingml_enumerationliteral) {
        this.thingml_enumerationliterals.add(thingml_enumerationliteral);
    }
    public thingML_TypeRef getThingml_typeref() {
        return thingml_typeref;
    }

    public void setThingml_typeref(thingML_TypeRef thingml_typeref) {
        this.thingml_typeref = thingml_typeref;
    }

}