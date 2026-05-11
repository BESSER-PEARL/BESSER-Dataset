





import java.util.List;
import java.util.ArrayList;

public class sxfm_Constraint  {

    private int id;





    private sxfm_ConstraintsSet sxfm_constraintsset;


    public sxfm_Constraint(
        int id    ) {
        this.id = id;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public sxfm_ConstraintsSet getSxfm_constraintsset() {
        return sxfm_constraintsset;
    }

    public void setSxfm_constraintsset(sxfm_ConstraintsSet sxfm_constraintsset) {
        this.sxfm_constraintsset = sxfm_constraintsset;
    }

}