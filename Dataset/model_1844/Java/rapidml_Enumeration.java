





import java.util.List;
import java.util.ArrayList;

public class rapidml_Enumeration extends SingleValueType {






    private List<rapidml_EnumConstant> rapidml_enumconstants;




    private rapidml_EnumConstant rapidml_enumconstant;




    private rapidml_PrimitiveType rapidml_primitivetype;


    public rapidml_Enumeration(
    ) {
        super(
        );
        this.rapidml_enumconstants = new ArrayList<>();
    }

    public rapidml_Enumeration(
        ArrayList<rapidml_EnumConstant> rapidml_enumconstants    ) {
        this.rapidml_enumconstants = rapidml_enumconstants;
    }


    public List<rapidml_EnumConstant> getRapidml_enumconstants() {
        return rapidml_enumconstants;
    }

    public void addRapidml_enumconstant(Rapidml_enumconstant rapidml_enumconstant) {
        this.rapidml_enumconstants.add(rapidml_enumconstant);
    }
    public rapidml_EnumConstant getRapidml_enumconstant() {
        return rapidml_enumconstant;
    }

    public void setRapidml_enumconstant(rapidml_EnumConstant rapidml_enumconstant) {
        this.rapidml_enumconstant = rapidml_enumconstant;
    }
    public rapidml_PrimitiveType getRapidml_primitivetype() {
        return rapidml_primitivetype;
    }

    public void setRapidml_primitivetype(rapidml_PrimitiveType rapidml_primitivetype) {
        this.rapidml_primitivetype = rapidml_primitivetype;
    }

}