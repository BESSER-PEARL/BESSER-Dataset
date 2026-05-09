





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Expression extends OpaqueExpression {

    private String symbol;





    private List<UML2WithID_ValueSpecification> uml2withid_valuespecifications;


    public UML2WithID_Expression(
        String symbol    ) {
        super(
        );
        this.symbol = symbol;
        this.uml2withid_valuespecifications = new ArrayList<>();
    }

    public UML2WithID_Expression(
        String symbol        ArrayList<UML2WithID_ValueSpecification> uml2withid_valuespecifications    ) {
        this.symbol = symbol;
        this.uml2withid_valuespecifications = uml2withid_valuespecifications;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public List<UML2WithID_ValueSpecification> getUml2withid_valuespecifications() {
        return uml2withid_valuespecifications;
    }

    public void addUml2withid_valuespecification(Uml2withid_valuespecification uml2withid_valuespecification) {
        this.uml2withid_valuespecifications.add(uml2withid_valuespecification);
    }

}