





import java.util.List;
import java.util.ArrayList;

public class fmp_Constraint  {

    private String text;





    private fmp_Feature fmp_feature;


    public fmp_Constraint(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public fmp_Feature getFmp_feature() {
        return fmp_feature;
    }

    public void setFmp_feature(fmp_Feature fmp_feature) {
        this.fmp_feature = fmp_feature;
    }

}