





import java.util.List;
import java.util.ArrayList;

public class atlstatic_OCL_RealExp extends NumericExp {

    private String realSymbol;



    public atlstatic_OCL_RealExp(
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