





import java.util.List;
import java.util.ArrayList;

public class pivot_FeatureCallExp extends CallExp {

    private String isPre;



    public pivot_FeatureCallExp(
        String isPre    ) {
        super(
        );
        this.isPre = isPre;
    }


    public String getIspre() {
        return isPre;
    }

    public void setIspre(String isPre) {
        this.isPre = isPre;
    }


}