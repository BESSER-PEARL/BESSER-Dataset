





import java.util.List;
import java.util.ArrayList;

public class types_JvmType extends JvmIdentifiableElement {






    private types_JvmAnyTypeReference types_jvmanytypereference;




    private types_JvmParameterizedTypeReference types_jvmparameterizedtypereference;




    private types_JvmCompoundTypeReference types_jvmcompoundtypereference;


    public types_JvmType(
    ) {
        super(
        );
    }



    public types_JvmAnyTypeReference getTypes_jvmanytypereference() {
        return types_jvmanytypereference;
    }

    public void setTypes_jvmanytypereference(types_JvmAnyTypeReference types_jvmanytypereference) {
        this.types_jvmanytypereference = types_jvmanytypereference;
    }
    public types_JvmParameterizedTypeReference getTypes_jvmparameterizedtypereference() {
        return types_jvmparameterizedtypereference;
    }

    public void setTypes_jvmparameterizedtypereference(types_JvmParameterizedTypeReference types_jvmparameterizedtypereference) {
        this.types_jvmparameterizedtypereference = types_jvmparameterizedtypereference;
    }
    public types_JvmCompoundTypeReference getTypes_jvmcompoundtypereference() {
        return types_jvmcompoundtypereference;
    }

    public void setTypes_jvmcompoundtypereference(types_JvmCompoundTypeReference types_jvmcompoundtypereference) {
        this.types_jvmcompoundtypereference = types_jvmcompoundtypereference;
    }

}