





import java.util.List;
import java.util.ArrayList;

public class JTLMM_essentialocl_RealLiteralExp extends NumericLiteralExp {

    private float realSymbol;



    public JTLMM_essentialocl_RealLiteralExp(
        float realSymbol    ) {
        super(
        );
        this.realSymbol = realSymbol;
    }


    public float getRealsymbol() {
        return realSymbol;
    }

    public void setRealsymbol(float realSymbol) {
        this.realSymbol = realSymbol;
    }


}