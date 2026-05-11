





import java.util.List;
import java.util.ArrayList;

public class smachDSL_StateMachine  {

    private String name;





    private smachDSL_PrimitivePackage smachdsl_primitivepackage;


    public smachDSL_StateMachine(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smachDSL_PrimitivePackage getSmachdsl_primitivepackage() {
        return smachdsl_primitivepackage;
    }

    public void setSmachdsl_primitivepackage(smachDSL_PrimitivePackage smachdsl_primitivepackage) {
        this.smachdsl_primitivepackage = smachdsl_primitivepackage;
    }

}