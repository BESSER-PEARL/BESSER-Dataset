





import java.util.List;
import java.util.ArrayList;

public class smif_values_UnitType extends ValueType {

    private String offset;
    private String symbol;
    private String ratio;



    public smif_values_UnitType(
        String offset,        String symbol,        String ratio    ) {
        super(
        );
        this.offset = offset;
        this.symbol = symbol;
        this.ratio = ratio;
    }


    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public String getRatio() {
        return ratio;
    }

    public void setRatio(String ratio) {
        this.ratio = ratio;
    }


}