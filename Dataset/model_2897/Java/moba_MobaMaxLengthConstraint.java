





import java.util.List;
import java.util.ArrayList;

public class moba_MobaMaxLengthConstraint extends MobaConstraint {

    private int filterValue;





    private moba_MobaConstant moba_mobaconstant;


    public moba_MobaMaxLengthConstraint(
        int filterValue    ) {
        super(
        );
        this.filterValue = filterValue;
    }


    public int getFiltervalue() {
        return filterValue;
    }

    public void setFiltervalue(int filterValue) {
        this.filterValue = filterValue;
    }

    public moba_MobaConstant getMoba_mobaconstant() {
        return moba_mobaconstant;
    }

    public void setMoba_mobaconstant(moba_MobaConstant moba_mobaconstant) {
        this.moba_mobaconstant = moba_mobaconstant;
    }

}