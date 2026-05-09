





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Expression extends ValueSpecification {

    private String symbol;





    private List<uml3_0_0_ValueSpecification> uml3_0_0_valuespecifications;


    public uml3_0_0_Expression(
        String symbol    ) {
        super(
        );
        this.symbol = symbol;
        this.uml3_0_0_valuespecifications = new ArrayList<>();
    }

    public uml3_0_0_Expression(
        String symbol        ArrayList<uml3_0_0_ValueSpecification> uml3_0_0_valuespecifications    ) {
        this.symbol = symbol;
        this.uml3_0_0_valuespecifications = uml3_0_0_valuespecifications;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public List<uml3_0_0_ValueSpecification> getUml3_0_0_valuespecifications() {
        return uml3_0_0_valuespecifications;
    }

    public void addUml3_0_0_valuespecification(Uml3_0_0_valuespecification uml3_0_0_valuespecification) {
        this.uml3_0_0_valuespecifications.add(uml3_0_0_valuespecification);
    }

}