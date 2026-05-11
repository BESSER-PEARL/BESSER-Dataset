





import java.util.List;
import java.util.ArrayList;

public class moba_MobaRegexpConstraint extends MobaConstraint {

    private String filterString;





    private moba_MobaConstant moba_mobaconstant;


    public moba_MobaRegexpConstraint(
        String filterString    ) {
        super(
        );
        this.filterString = filterString;
    }


    public String getFilterstring() {
        return filterString;
    }

    public void setFilterstring(String filterString) {
        this.filterString = filterString;
    }

    public moba_MobaConstant getMoba_mobaconstant() {
        return moba_mobaconstant;
    }

    public void setMoba_mobaconstant(moba_MobaConstant moba_mobaconstant) {
        this.moba_mobaconstant = moba_mobaconstant;
    }

}