





import java.util.List;
import java.util.ArrayList;

public class moba_MobaMinConstraint extends MobaConstraint {

    private float filterValue;





    private moba_MobaConstant moba_mobaconstant;


    public moba_MobaMinConstraint(
        float filterValue    ) {
        super(
        );
        this.filterValue = filterValue;
    }


    public float getFiltervalue() {
        return filterValue;
    }

    public void setFiltervalue(float filterValue) {
        this.filterValue = filterValue;
    }

    public moba_MobaConstant getMoba_mobaconstant() {
        return moba_mobaconstant;
    }

    public void setMoba_mobaconstant(moba_MobaConstant moba_mobaconstant) {
        this.moba_mobaconstant = moba_mobaconstant;
    }

}