





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit  {

    private String name;
    private String description;
    private String definitionURI;
    private String symbol;





    private List<QuantityKind> quantitykinds;


    public SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit(
        String name,        String description,        String definitionURI,        String symbol    ) {
        this.name = name;
        this.description = description;
        this.definitionURI = definitionURI;
        this.symbol = symbol;
        this.quantitykinds = new ArrayList<>();
    }

    public SysML_ValueTypes_QUDV_UnitAndQuantityKind_Unit(
        String name,        String description,        String definitionURI,        String symbol        ArrayList<QuantityKind> quantitykinds    ) {
        this.name = name;
        this.description = description;
        this.definitionURI = definitionURI;
        this.symbol = symbol;
        this.quantitykinds = quantitykinds;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDefinitionuri() {
        return definitionURI;
    }

    public void setDefinitionuri(String definitionURI) {
        this.definitionURI = definitionURI;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public List<QuantityKind> getQuantitykinds() {
        return quantitykinds;
    }

    public void addQuantitykind(Quantitykind quantitykind) {
        this.quantitykinds.add(quantitykind);
    }

}