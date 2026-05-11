





import java.util.List;
import java.util.ArrayList;

public class gx10_Referentiable  {

    private String name;





    private gx10_BoolVar gx10_boolvar;




    private gx10_BoolVarAccess gx10_boolvaraccess;




    private gx10_Method gx10_method;


    public gx10_Referentiable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gx10_BoolVar getGx10_boolvar() {
        return gx10_boolvar;
    }

    public void setGx10_boolvar(gx10_BoolVar gx10_boolvar) {
        this.gx10_boolvar = gx10_boolvar;
    }
    public gx10_BoolVarAccess getGx10_boolvaraccess() {
        return gx10_boolvaraccess;
    }

    public void setGx10_boolvaraccess(gx10_BoolVarAccess gx10_boolvaraccess) {
        this.gx10_boolvaraccess = gx10_boolvaraccess;
    }
    public gx10_Method getGx10_method() {
        return gx10_method;
    }

    public void setGx10_method(gx10_Method gx10_method) {
        this.gx10_method = gx10_method;
    }

}