





import java.util.List;
import java.util.ArrayList;

public class types_Metaclass extends RefType {

    private String name;
    private boolean explicitOcurrence;





    private types_BooleanType types_booleantype;


    public types_Metaclass(
        String name,        boolean explicitOcurrence    ) {
        super(
        );
        this.name = name;
        this.explicitOcurrence = explicitOcurrence;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getExplicitocurrence() {
        return explicitOcurrence;
    }

    public void setExplicitocurrence(boolean explicitOcurrence) {
        this.explicitOcurrence = explicitOcurrence;
    }

    public types_BooleanType getTypes_booleantype() {
        return types_booleantype;
    }

    public void setTypes_booleantype(types_BooleanType types_booleantype) {
        this.types_booleantype = types_booleantype;
    }

}