





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities  {

    private String symbol;
    private String name;
    private String description;
    private String definitionURI;





    private List<QuantityKind> quantitykinds;




    private List<QuantityKind> quantitykinds;




    private List<SystemOfQuantities> systemofquantitiess;




    private List<SystemOfQuantities> systemofquantitiess;


    public SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities(
        String symbol,        String name,        String description,        String definitionURI    ) {
        this.symbol = symbol;
        this.name = name;
        this.description = description;
        this.definitionURI = definitionURI;
        this.quantitykinds = new ArrayList<>();
        this.quantitykinds = new ArrayList<>();
        this.systemofquantitiess = new ArrayList<>();
        this.systemofquantitiess = new ArrayList<>();
    }

    public SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities(
        String symbol,        String name,        String description,        String definitionURI        ArrayList<QuantityKind> quantitykinds,        ArrayList<QuantityKind> quantitykinds,        ArrayList<SystemOfQuantities> systemofquantitiess,        ArrayList<SystemOfQuantities> systemofquantitiess    ) {
        this.symbol = symbol;
        this.name = name;
        this.description = description;
        this.definitionURI = definitionURI;
        this.quantitykinds = quantitykinds;
        this.quantitykinds = quantitykinds;
        this.systemofquantitiess = systemofquantitiess;
        this.systemofquantitiess = systemofquantitiess;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
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

    public List<QuantityKind> getQuantitykinds() {
        return quantitykinds;
    }

    public void addQuantitykind(Quantitykind quantitykind) {
        this.quantitykinds.add(quantitykind);
    }
    public List<QuantityKind> getQuantitykinds() {
        return quantitykinds;
    }

    public void addQuantitykind(Quantitykind quantitykind) {
        this.quantitykinds.add(quantitykind);
    }
    public List<SystemOfQuantities> getSystemofquantitiess() {
        return systemofquantitiess;
    }

    public void addSystemofquantities(Systemofquantities systemofquantities) {
        this.systemofquantitiess.add(systemofquantities);
    }
    public List<SystemOfQuantities> getSystemofquantitiess() {
        return systemofquantitiess;
    }

    public void addSystemofquantities(Systemofquantities systemofquantities) {
        this.systemofquantitiess.add(systemofquantities);
    }

}