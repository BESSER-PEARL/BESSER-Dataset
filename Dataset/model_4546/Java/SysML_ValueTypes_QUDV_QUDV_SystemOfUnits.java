





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_SystemOfUnits  {

    private String name;
    private String description;
    private String symbol;
    private String definitionURI;





    private SystemOfQuantities systemofquantities;




    private List<SystemOfUnits> systemofunitss;




    private List<Unit> units;




    private List<Prefix> prefixs;




    private List<SystemOfUnits> systemofunitss;




    private List<Unit> units;


    public SysML_ValueTypes_QUDV_QUDV_SystemOfUnits(
        String name,        String description,        String symbol,        String definitionURI    ) {
        this.name = name;
        this.description = description;
        this.symbol = symbol;
        this.definitionURI = definitionURI;
        this.systemofunitss = new ArrayList<>();
        this.units = new ArrayList<>();
        this.prefixs = new ArrayList<>();
        this.systemofunitss = new ArrayList<>();
        this.units = new ArrayList<>();
    }

    public SysML_ValueTypes_QUDV_QUDV_SystemOfUnits(
        String name,        String description,        String symbol,        String definitionURI        ArrayList<SystemOfUnits> systemofunitss,        ArrayList<Unit> units,        ArrayList<Prefix> prefixs,        ArrayList<SystemOfUnits> systemofunitss,        ArrayList<Unit> units    ) {
        this.name = name;
        this.description = description;
        this.symbol = symbol;
        this.definitionURI = definitionURI;
        this.systemofunitss = systemofunitss;
        this.units = units;
        this.prefixs = prefixs;
        this.systemofunitss = systemofunitss;
        this.units = units;
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

    public SystemOfQuantities getSystemofquantities() {
        return systemofquantities;
    }

    public void setSystemofquantities(SystemOfQuantities systemofquantities) {
        this.systemofquantities = systemofquantities;
    }
    public List<SystemOfUnits> getSystemofunitss() {
        return systemofunitss;
    }

    public void addSystemofunits(Systemofunits systemofunits) {
        this.systemofunitss.add(systemofunits);
    }
    public List<Unit> getUnits() {
        return units;
    }

    public void addUnit(Unit unit) {
        this.units.add(unit);
    }
    public List<Prefix> getPrefixs() {
        return prefixs;
    }

    public void addPrefix(Prefix prefix) {
        this.prefixs.add(prefix);
    }
    public List<SystemOfUnits> getSystemofunitss() {
        return systemofunitss;
    }

    public void addSystemofunits(Systemofunits systemofunits) {
        this.systemofunitss.add(systemofunits);
    }
    public List<Unit> getUnits() {
        return units;
    }

    public void addUnit(Unit unit) {
        this.units.add(unit);
    }

}