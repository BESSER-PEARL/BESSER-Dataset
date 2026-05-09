





import java.util.List;
import java.util.ArrayList;

public class gastm_RealType extends NumberType {

    private String precision;



    public gastm_RealType(
        String precision    ) {
        super(
        );
        this.precision = precision;
    }


    public String getPrecision() {
        return precision;
    }

    public void setPrecision(String precision) {
        this.precision = precision;
    }


}