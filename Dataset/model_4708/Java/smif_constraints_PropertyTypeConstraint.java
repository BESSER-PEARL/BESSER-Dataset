





import java.util.List;
import java.util.ArrayList;

public class smif_constraints_PropertyTypeConstraint extends PropertyConstraint {

    private String prerequisiteType;





    private Type type;


    public smif_constraints_PropertyTypeConstraint(
        String prerequisiteType    ) {
        super(
        );
        this.prerequisiteType = prerequisiteType;
    }


    public String getPrerequisitetype() {
        return prerequisiteType;
    }

    public void setPrerequisitetype(String prerequisiteType) {
        this.prerequisiteType = prerequisiteType;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type type) {
        this.type = type;
    }

}