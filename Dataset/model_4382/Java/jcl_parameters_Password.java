





import java.util.List;
import java.util.ArrayList;

public class jcl_parameters_Password extends Parameter {

    private String old;
    private String new;



    public jcl_parameters_Password(
        String old,        String new    ) {
        super(
        );
        this.old = old;
        this.new = new;
    }


    public String getOld() {
        return old;
    }

    public void setOld(String old) {
        this.old = old;
    }
    public String getNew() {
        return new;
    }

    public void setNew(String new) {
        this.new = new;
    }


}