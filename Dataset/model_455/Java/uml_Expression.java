





import java.util.List;
import java.util.ArrayList;

public class uml_Expression extends ValueSpecification {

    private String symbol;





    private List<uml_ValueSpecification> uml_valuespecifications;


    public uml_Expression(
        String symbol    ) {
        super(
        );
        this.symbol = symbol;
        this.uml_valuespecifications = new ArrayList<>();
    }

    public uml_Expression(
        String symbol        ArrayList<uml_ValueSpecification> uml_valuespecifications    ) {
        this.symbol = symbol;
        this.uml_valuespecifications = uml_valuespecifications;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public List<uml_ValueSpecification> getUml_valuespecifications() {
        return uml_valuespecifications;
    }

    public void addUml_valuespecification(Uml_valuespecification uml_valuespecification) {
        this.uml_valuespecifications.add(uml_valuespecification);
    }

}