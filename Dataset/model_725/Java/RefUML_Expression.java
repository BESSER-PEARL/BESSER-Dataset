





import java.util.List;
import java.util.ArrayList;

public class RefUML_Expression extends ValueSpecification {

    private String symbol;





    private List<RefUML_ValueSpecification> refuml_valuespecifications;


    public RefUML_Expression(
        String symbol    ) {
        super(
        );
        this.symbol = symbol;
        this.refuml_valuespecifications = new ArrayList<>();
    }

    public RefUML_Expression(
        String symbol        ArrayList<RefUML_ValueSpecification> refuml_valuespecifications    ) {
        this.symbol = symbol;
        this.refuml_valuespecifications = refuml_valuespecifications;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public List<RefUML_ValueSpecification> getRefuml_valuespecifications() {
        return refuml_valuespecifications;
    }

    public void addRefuml_valuespecification(Refuml_valuespecification refuml_valuespecification) {
        this.refuml_valuespecifications.add(refuml_valuespecification);
    }

}