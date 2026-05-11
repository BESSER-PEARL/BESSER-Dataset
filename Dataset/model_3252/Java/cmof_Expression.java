





import java.util.List;
import java.util.ArrayList;

public class cmof_Expression extends ValueSpecification {

    private String symbol;





    private List<cmof_ValueSpecification> cmof_valuespecifications;


    public cmof_Expression(
        String symbol    ) {
        super(
        );
        this.symbol = symbol;
        this.cmof_valuespecifications = new ArrayList<>();
    }

    public cmof_Expression(
        String symbol        ArrayList<cmof_ValueSpecification> cmof_valuespecifications    ) {
        this.symbol = symbol;
        this.cmof_valuespecifications = cmof_valuespecifications;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public List<cmof_ValueSpecification> getCmof_valuespecifications() {
        return cmof_valuespecifications;
    }

    public void addCmof_valuespecification(Cmof_valuespecification cmof_valuespecification) {
        this.cmof_valuespecifications.add(cmof_valuespecification);
    }

}