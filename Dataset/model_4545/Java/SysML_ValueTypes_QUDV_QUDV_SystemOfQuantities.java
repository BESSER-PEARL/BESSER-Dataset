





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities  {

    private String definitionURI;
    private boolean name;
    private String description;
    private String symbol;





    private List<SystemOfQuantities> systemofquantitiess;




    private List<QuantityKind> quantitykinds;




    private List<SystemOfQuantities> systemofquantitiess;




    private List<QuantityKind> quantitykinds;


    public SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities(
        String definitionURI,        boolean name,        String description,        String symbol    ) {
        this.definitionURI = definitionURI;
        this.name = name;
        this.description = description;
        this.symbol = symbol;
        this.systemofquantitiess = new ArrayList<>();
        this.quantitykinds = new ArrayList<>();
        this.systemofquantitiess = new ArrayList<>();
        this.quantitykinds = new ArrayList<>();
    }

    public SysML_ValueTypes_QUDV_QUDV_SystemOfQuantities(
        String definitionURI,        boolean name,        String description,        String symbol        ArrayList<SystemOfQuantities> systemofquantitiess,        ArrayList<QuantityKind> quantitykinds,        ArrayList<SystemOfQuantities> systemofquantitiess,        ArrayList<QuantityKind> quantitykinds    ) {
        this.definitionURI = definitionURI;
        this.name = name;
        this.description = description;
        this.symbol = symbol;
        this.systemofquantitiess = systemofquantitiess;
        this.quantitykinds = quantitykinds;
        this.systemofquantitiess = systemofquantitiess;
        this.quantitykinds = quantitykinds;
    }

    public String getDefinitionuri() {
        return definitionURI;
    }

    public void setDefinitionuri(String definitionURI) {
        this.definitionURI = definitionURI;
    }
    public boolean getName() {
        return name;
    }

    public void setName(boolean name) {
        this.name = name;
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

    public List<SystemOfQuantities> getSystemofquantitiess() {
        return systemofquantitiess;
    }

    public void addSystemofquantities(Systemofquantities systemofquantities) {
        this.systemofquantitiess.add(systemofquantities);
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
    public List<QuantityKind> getQuantitykinds() {
        return quantitykinds;
    }

    public void addQuantitykind(Quantitykind quantitykind) {
        this.quantitykinds.add(quantitykind);
    }

}