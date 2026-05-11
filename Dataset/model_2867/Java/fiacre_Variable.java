





import java.util.List;
import java.util.ArrayList;

public class fiacre_Variable  {

    private String name;





    private fiacre_VarRef fiacre_varref;




    private fiacre_RefArg fiacre_refarg;




    private fiacre_Type fiacre_type;


    public fiacre_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fiacre_VarRef getFiacre_varref() {
        return fiacre_varref;
    }

    public void setFiacre_varref(fiacre_VarRef fiacre_varref) {
        this.fiacre_varref = fiacre_varref;
    }
    public fiacre_RefArg getFiacre_refarg() {
        return fiacre_refarg;
    }

    public void setFiacre_refarg(fiacre_RefArg fiacre_refarg) {
        this.fiacre_refarg = fiacre_refarg;
    }
    public fiacre_Type getFiacre_type() {
        return fiacre_type;
    }

    public void setFiacre_type(fiacre_Type fiacre_type) {
        this.fiacre_type = fiacre_type;
    }

}