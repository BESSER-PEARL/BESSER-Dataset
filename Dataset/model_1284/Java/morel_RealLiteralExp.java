





import java.util.List;
import java.util.ArrayList;

public class morel_RealLiteralExp extends LiteralExp {

    private float realSymbol;



    public morel_RealLiteralExp(
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