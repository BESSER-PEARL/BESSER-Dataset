





import java.util.List;
import java.util.ArrayList;

public class smif_values_UnitType extends ValueType {

    private String symbol;
    private String offset;
    private String ratio;



    public smif_values_UnitType(
        String symbol,        String offset,        String ratio    ) {
        super(
        );
        this.symbol = symbol;
        this.offset = offset;
        this.ratio = ratio;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }
    public String getRatio() {
        return ratio;
    }

    public void setRatio(String ratio) {
        this.ratio = ratio;
    }


}