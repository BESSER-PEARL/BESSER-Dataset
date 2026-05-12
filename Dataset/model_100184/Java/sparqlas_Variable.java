





import java.util.List;
import java.util.ArrayList;

public class sparqlas_Variable extends Term {

    private String symbol;





    private sparqlas_SelectQuery sparqlas_selectquery;


    public sparqlas_Variable(
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

    public sparqlas_SelectQuery getSparqlas_selectquery() {
        return sparqlas_selectquery;
    }

    public void setSparqlas_selectquery(sparqlas_SelectQuery sparqlas_selectquery) {
        this.sparqlas_selectquery = sparqlas_selectquery;
    }

}