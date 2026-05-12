





import java.util.List;
import java.util.ArrayList;

public class UML2_Expression extends OpaqueExpression {

    private String symbol;





    private List<UML2_ValueSpecification> uml2_valuespecifications;


    public UML2_Expression(
        String symbol    ) {
        super(
        );
        this.symbol = symbol;
        this.uml2_valuespecifications = new ArrayList<>();
    }

    public UML2_Expression(
        String symbol        ArrayList<UML2_ValueSpecification> uml2_valuespecifications    ) {
        this.symbol = symbol;
        this.uml2_valuespecifications = uml2_valuespecifications;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public List<UML2_ValueSpecification> getUml2_valuespecifications() {
        return uml2_valuespecifications;
    }

    public void addUml2_valuespecification(Uml2_valuespecification uml2_valuespecification) {
        this.uml2_valuespecifications.add(uml2_valuespecification);
    }

}