





import java.util.List;
import java.util.ArrayList;

public class gastm_EnumType extends DataType {






    private List<gastm_EnumLiteralDefinition> gastm_enumliteraldefinitions;




    private gastm_EnumTypeDefinition gastm_enumtypedefinition;


    public gastm_EnumType(
    ) {
        super(
        );
        this.gastm_enumliteraldefinitions = new ArrayList<>();
    }

    public gastm_EnumType(
        ArrayList<gastm_EnumLiteralDefinition> gastm_enumliteraldefinitions    ) {
        this.gastm_enumliteraldefinitions = gastm_enumliteraldefinitions;
    }


    public List<gastm_EnumLiteralDefinition> getGastm_enumliteraldefinitions() {
        return gastm_enumliteraldefinitions;
    }

    public void addGastm_enumliteraldefinition(Gastm_enumliteraldefinition gastm_enumliteraldefinition) {
        this.gastm_enumliteraldefinitions.add(gastm_enumliteraldefinition);
    }
    public gastm_EnumTypeDefinition getGastm_enumtypedefinition() {
        return gastm_enumtypedefinition;
    }

    public void setGastm_enumtypedefinition(gastm_EnumTypeDefinition gastm_enumtypedefinition) {
        this.gastm_enumtypedefinition = gastm_enumtypedefinition;
    }

}