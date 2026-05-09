





import java.util.List;
import java.util.ArrayList;

public class express_core_RealType extends NumericType {

    private String precision;



    public express_core_RealType(
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