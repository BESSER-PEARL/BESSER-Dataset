





import java.util.List;
import java.util.ArrayList;

public class rcd_Class extends Classifier {

    private boolean is_persistent;





    private rcd_Class rcd_class;




    private rcd_Association rcd_association;




    private rcd_Association rcd_association;


    public rcd_Class(
        boolean is_persistent    ) {
        super(
        );
        this.is_persistent = is_persistent;
    }


    public boolean getIs_persistent() {
        return is_persistent;
    }

    public void setIs_persistent(boolean is_persistent) {
        this.is_persistent = is_persistent;
    }

    public rcd_Class getRcd_class() {
        return rcd_class;
    }

    public void setRcd_class(rcd_Class rcd_class) {
        this.rcd_class = rcd_class;
    }
    public rcd_Association getRcd_association() {
        return rcd_association;
    }

    public void setRcd_association(rcd_Association rcd_association) {
        this.rcd_association = rcd_association;
    }
    public rcd_Association getRcd_association() {
        return rcd_association;
    }

    public void setRcd_association(rcd_Association rcd_association) {
        this.rcd_association = rcd_association;
    }

}