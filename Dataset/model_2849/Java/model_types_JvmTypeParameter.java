





import java.util.List;
import java.util.ArrayList;

public class model_types_JvmTypeParameter extends types_JvmConstraintOwner, types_JvmComponentType {

    private String name;



    public model_types_JvmTypeParameter(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}