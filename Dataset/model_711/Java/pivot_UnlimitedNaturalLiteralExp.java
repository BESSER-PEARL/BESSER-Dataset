





import java.util.List;
import java.util.ArrayList;

public class pivot_UnlimitedNaturalLiteralExp extends NumericLiteralExp {

    private String unlimitedNaturalSymbol;



    public pivot_UnlimitedNaturalLiteralExp(
        String unlimitedNaturalSymbol    ) {
        super(
        );
        this.unlimitedNaturalSymbol = unlimitedNaturalSymbol;
    }


    public String getUnlimitednaturalsymbol() {
        return unlimitedNaturalSymbol;
    }

    public void setUnlimitednaturalsymbol(String unlimitedNaturalSymbol) {
        this.unlimitedNaturalSymbol = unlimitedNaturalSymbol;
    }


}