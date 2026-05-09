





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_RealLiteralExpCS extends PrimitiveLiteralExpCS {

    private String realSymbol;



    public ocl_cst_RealLiteralExpCS(
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