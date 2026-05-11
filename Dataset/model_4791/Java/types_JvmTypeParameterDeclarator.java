





import java.util.List;
import java.util.ArrayList;

public class types_JvmTypeParameterDeclarator  {






    private List<types_JvmTypeParameter> types_jvmtypeparameters;




    private types_JvmTypeParameter types_jvmtypeparameter;


    public types_JvmTypeParameterDeclarator(
    ) {
        this.types_jvmtypeparameters = new ArrayList<>();
    }

    public types_JvmTypeParameterDeclarator(
        ArrayList<types_JvmTypeParameter> types_jvmtypeparameters    ) {
        this.types_jvmtypeparameters = types_jvmtypeparameters;
    }


    public List<types_JvmTypeParameter> getTypes_jvmtypeparameters() {
        return types_jvmtypeparameters;
    }

    public void addTypes_jvmtypeparameter(Types_jvmtypeparameter types_jvmtypeparameter) {
        this.types_jvmtypeparameters.add(types_jvmtypeparameter);
    }
    public types_JvmTypeParameter getTypes_jvmtypeparameter() {
        return types_jvmtypeparameter;
    }

    public void setTypes_jvmtypeparameter(types_JvmTypeParameter types_jvmtypeparameter) {
        this.types_jvmtypeparameter = types_jvmtypeparameter;
    }

}