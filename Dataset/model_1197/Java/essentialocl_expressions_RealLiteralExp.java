





import java.util.List;
import java.util.ArrayList;

public class essentialocl_expressions_RealLiteralExp extends NumericLiteralExp {

    private String realSymbol;



    public essentialocl_expressions_RealLiteralExp(
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