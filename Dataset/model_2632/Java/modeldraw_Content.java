





import java.util.List;
import java.util.ArrayList;

public class modeldraw_Content extends NamedItem {

    private String symbol;



    public modeldraw_Content(
        String symbol    ) {
        super(
        );
        this.symbol = symbol;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }


}