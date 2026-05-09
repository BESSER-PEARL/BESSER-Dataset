





import java.util.List;
import java.util.ArrayList;

public class OCLinEmig_RealExp extends NumericExp {

    private String realSymbol;



    public OCLinEmig_RealExp(
        String realSymbol    ) {
        super(
        );
        this.realSymbol = realSymbol;
    }


    public String getRealsymbol() {
        return realSymbol;
    }

    public void setRealsymbol(String realSymbol) {
        this.realSymbol = realSymbol;
    }


}