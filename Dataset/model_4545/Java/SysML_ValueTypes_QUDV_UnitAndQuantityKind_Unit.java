





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit  {

    private String description;
    private String symbol;
    private String definitionURI;
    private String name;





    private List<QuantityKind> quantitykinds;


    public SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit(
        String description,        String symbol,        String definitionURI,        String name    ) {
        this.description = description;
        this.symbol = symbol;
        this.definitionURI = definitionURI;
        this.name = name;
        this.quantitykinds = new ArrayList<>();
    }

    public SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit(
        String description,        String symbol,        String definitionURI,        String name        ArrayList<QuantityKind> quantitykinds    ) {
        this.description = description;
        this.symbol = symbol;
        this.definitionURI = definitionURI;
        this.name = name;
        this.quantitykinds = quantitykinds;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public String getDefinitionuri() {
        return definitionURI;
    }

    public void setDefinitionuri(String definitionURI) {
        this.definitionURI = definitionURI;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<QuantityKind> getQuantitykinds() {
        return quantitykinds;
    }

    public void addQuantitykind(Quantitykind quantitykind) {
        this.quantitykinds.add(quantitykind);
    }

}