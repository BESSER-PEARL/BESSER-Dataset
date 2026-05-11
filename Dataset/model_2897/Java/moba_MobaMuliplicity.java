





import java.util.List;
import java.util.ArrayList;

public class moba_MobaMuliplicity  {

    private String lower;
    private String upper;





    private moba_MobaMultiplicityAble moba_mobamultiplicityable;


    public moba_MobaMuliplicity(
        String lower,        String upper    ) {
        this.lower = lower;
        this.upper = upper;
    }


    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }

    public moba_MobaMultiplicityAble getMoba_mobamultiplicityable() {
        return moba_mobamultiplicityable;
    }

    public void setMoba_mobamultiplicityable(moba_MobaMultiplicityAble moba_mobamultiplicityable) {
        this.moba_mobamultiplicityable = moba_mobamultiplicityable;
    }

}