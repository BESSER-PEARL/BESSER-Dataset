





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER  {






    private List<QuantityKindFactor> quantitykindfactors;




    private List<Prefix> prefixs;




    private List<Dimension> dimensions;




    private List<SystemOfUnits> systemofunitss;




    private List<SystemOfQuantities> systemofquantitiess;


    public SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER(
    ) {
        this.quantitykindfactors = new ArrayList<>();
        this.prefixs = new ArrayList<>();
        this.dimensions = new ArrayList<>();
        this.systemofunitss = new ArrayList<>();
        this.systemofquantitiess = new ArrayList<>();
    }

    public SysML_ValueTypes_QUDV_ROOT_RESOURCE_SHAPE_CONTAINER(
        ArrayList<QuantityKindFactor> quantitykindfactors,        ArrayList<Prefix> prefixs,        ArrayList<Dimension> dimensions,        ArrayList<SystemOfUnits> systemofunitss,        ArrayList<SystemOfQuantities> systemofquantitiess    ) {
        this.quantitykindfactors = quantitykindfactors;
        this.prefixs = prefixs;
        this.dimensions = dimensions;
        this.systemofunitss = systemofunitss;
        this.systemofquantitiess = systemofquantitiess;
    }


    public List<QuantityKindFactor> getQuantitykindfactors() {
        return quantitykindfactors;
    }

    public void addQuantitykindfactor(Quantitykindfactor quantitykindfactor) {
        this.quantitykindfactors.add(quantitykindfactor);
    }
    public List<Prefix> getPrefixs() {
        return prefixs;
    }

    public void addPrefix(Prefix prefix) {
        this.prefixs.add(prefix);
    }
    public List<Dimension> getDimensions() {
        return dimensions;
    }

    public void addDimension(Dimension dimension) {
        this.dimensions.add(dimension);
    }
    public List<SystemOfUnits> getSystemofunitss() {
        return systemofunitss;
    }

    public void addSystemofunits(Systemofunits systemofunits) {
        this.systemofunitss.add(systemofunits);
    }
    public List<SystemOfQuantities> getSystemofquantitiess() {
        return systemofquantitiess;
    }

    public void addSystemofquantities(Systemofquantities systemofquantities) {
        this.systemofquantitiess.add(systemofquantities);
    }

}