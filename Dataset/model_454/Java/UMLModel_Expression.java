





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Expression extends ValueSpecification {

    private String symbol;





    private List<UMLModel_ValueSpecification> umlmodel_valuespecifications;


    public UMLModel_Expression(
        String symbol    ) {
        super(
        );
        this.symbol = symbol;
        this.umlmodel_valuespecifications = new ArrayList<>();
    }

    public UMLModel_Expression(
        String symbol        ArrayList<UMLModel_ValueSpecification> umlmodel_valuespecifications    ) {
        this.symbol = symbol;
        this.umlmodel_valuespecifications = umlmodel_valuespecifications;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public List<UMLModel_ValueSpecification> getUmlmodel_valuespecifications() {
        return umlmodel_valuespecifications;
    }

    public void addUmlmodel_valuespecification(Umlmodel_valuespecification umlmodel_valuespecification) {
        this.umlmodel_valuespecifications.add(umlmodel_valuespecification);
    }

}