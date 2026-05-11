





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_SystemOfUnits  {

    private String name;
    private String definitionURI;
    private String description;
    private String symbol;





    private SystemOfQuantities systemofquantities;




    private List<Prefix> prefixs;




    private List<SystemOfUnits> systemofunitss;




    private List<SystemOfUnits> systemofunitss;




    private List<Unit> units;




    private List<Unit> units;


    public SysML_ValueTypes_QUDV_QUDV_SystemOfUnits(
        String name,        String definitionURI,        String description,        String symbol    ) {
        this.name = name;
        this.definitionURI = definitionURI;
        this.description = description;
        this.symbol = symbol;
        this.prefixs = new ArrayList<>();
        this.systemofunitss = new ArrayList<>();
        this.systemofunitss = new ArrayList<>();
        this.units = new ArrayList<>();
        this.units = new ArrayList<>();
    }

    public SysML_ValueTypes_QUDV_QUDV_SystemOfUnits(
        String name,        String definitionURI,        String description,        String symbol        ArrayList<Prefix> prefixs,        ArrayList<SystemOfUnits> systemofunitss,        ArrayList<SystemOfUnits> systemofunitss,        ArrayList<Unit> units,        ArrayList<Unit> units    ) {
        this.name = name;
        this.definitionURI = definitionURI;
        this.description = description;
        this.symbol = symbol;
        this.prefixs = prefixs;
        this.systemofunitss = systemofunitss;
        this.systemofunitss = systemofunitss;
        this.units = units;
        this.units = units;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDefinitionuri() {
        return definitionURI;
    }

    public void setDefinitionuri(String definitionURI) {
        this.definitionURI = definitionURI;
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

    public SystemOfQuantities getSystemofquantities() {
        return systemofquantities;
    }

    public void setSystemofquantities(SystemOfQuantities systemofquantities) {
        this.systemofquantities = systemofquantities;
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
    public List<Unit> getUnits() {
        return units;
    }

    public void addUnit(Unit unit) {
        this.units.add(unit);
    }

}