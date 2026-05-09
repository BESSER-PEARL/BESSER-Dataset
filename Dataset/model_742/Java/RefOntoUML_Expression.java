





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Expression extends ValueSpecification {

    private String symbol;





    private List<RefOntoUML_ValueSpecification> refontouml_valuespecifications;


    public RefOntoUML_Expression(
        String symbol    ) {
        super(
        );
        this.symbol = symbol;
        this.refontouml_valuespecifications = new ArrayList<>();
    }

    public RefOntoUML_Expression(
        String symbol        ArrayList<RefOntoUML_ValueSpecification> refontouml_valuespecifications    ) {
        this.symbol = symbol;
        this.refontouml_valuespecifications = refontouml_valuespecifications;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public List<RefOntoUML_ValueSpecification> getRefontouml_valuespecifications() {
        return refontouml_valuespecifications;
    }

    public void addRefontouml_valuespecification(Refontouml_valuespecification refontouml_valuespecification) {
        this.refontouml_valuespecifications.add(refontouml_valuespecification);
    }

}