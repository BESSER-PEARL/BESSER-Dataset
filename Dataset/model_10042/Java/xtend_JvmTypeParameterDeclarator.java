





import java.util.List;
import java.util.ArrayList;

public class xtend_JvmTypeParameterDeclarator  {






    private List<xtend_JvmTypeParameter> xtend_jvmtypeparameters;




    private xtend_JvmTypeParameter xtend_jvmtypeparameter;


    public xtend_JvmTypeParameterDeclarator(
    ) {
        this.xtend_jvmtypeparameters = new ArrayList<>();
    }

    public xtend_JvmTypeParameterDeclarator(
        ArrayList<xtend_JvmTypeParameter> xtend_jvmtypeparameters    ) {
        this.xtend_jvmtypeparameters = xtend_jvmtypeparameters;
    }


    public List<xtend_JvmTypeParameter> getXtend_jvmtypeparameters() {
        return xtend_jvmtypeparameters;
    }

    public void addXtend_jvmtypeparameter(Xtend_jvmtypeparameter xtend_jvmtypeparameter) {
        this.xtend_jvmtypeparameters.add(xtend_jvmtypeparameter);
    }
    public xtend_JvmTypeParameter getXtend_jvmtypeparameter() {
        return xtend_jvmtypeparameter;
    }

    public void setXtend_jvmtypeparameter(xtend_JvmTypeParameter xtend_jvmtypeparameter) {
        this.xtend_jvmtypeparameter = xtend_jvmtypeparameter;
    }

}