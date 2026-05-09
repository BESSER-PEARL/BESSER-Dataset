





import java.util.List;
import java.util.ArrayList;

public class MetaModelGraph_SubGraph  {

    private int amountOfParentEClass;
    private int amountRecursionUnits;
    private int amountOfAbstractEClass;
    private int amountOfConcreteEClass;
    private int amountPackages;
    private int amountEClassesOut;
    private int amountOfParentAbstractEClass;
    private int amountUnits;
    private int height;
    private int amountOfRecursionPackages;





    private MetaModelGraph_Graph metamodelgraph_graph;


    public MetaModelGraph_SubGraph(
        int amountOfParentEClass,        int amountRecursionUnits,        int amountOfAbstractEClass,        int amountOfConcreteEClass,        int amountPackages,        int amountEClassesOut,        int amountOfParentAbstractEClass,        int amountUnits,        int height,        int amountOfRecursionPackages    ) {
        this.amountOfParentEClass = amountOfParentEClass;
        this.amountRecursionUnits = amountRecursionUnits;
        this.amountOfAbstractEClass = amountOfAbstractEClass;
        this.amountOfConcreteEClass = amountOfConcreteEClass;
        this.amountPackages = amountPackages;
        this.amountEClassesOut = amountEClassesOut;
        this.amountOfParentAbstractEClass = amountOfParentAbstractEClass;
        this.amountUnits = amountUnits;
        this.height = height;
        this.amountOfRecursionPackages = amountOfRecursionPackages;
    }


    public int getAmountofparenteclass() {
        return amountOfParentEClass;
    }

    public void setAmountofparenteclass(int amountOfParentEClass) {
        this.amountOfParentEClass = amountOfParentEClass;
    }
    public int getAmountrecursionunits() {
        return amountRecursionUnits;
    }

    public void setAmountrecursionunits(int amountRecursionUnits) {
        this.amountRecursionUnits = amountRecursionUnits;
    }
    public int getAmountofabstracteclass() {
        return amountOfAbstractEClass;
    }

    public void setAmountofabstracteclass(int amountOfAbstractEClass) {
        this.amountOfAbstractEClass = amountOfAbstractEClass;
    }
    public int getAmountofconcreteeclass() {
        return amountOfConcreteEClass;
    }

    public void setAmountofconcreteeclass(int amountOfConcreteEClass) {
        this.amountOfConcreteEClass = amountOfConcreteEClass;
    }
    public int getAmountpackages() {
        return amountPackages;
    }

    public void setAmountpackages(int amountPackages) {
        this.amountPackages = amountPackages;
    }
    public int getAmounteclassesout() {
        return amountEClassesOut;
    }

    public void setAmounteclassesout(int amountEClassesOut) {
        this.amountEClassesOut = amountEClassesOut;
    }
    public int getAmountofparentabstracteclass() {
        return amountOfParentAbstractEClass;
    }

    public void setAmountofparentabstracteclass(int amountOfParentAbstractEClass) {
        this.amountOfParentAbstractEClass = amountOfParentAbstractEClass;
    }
    public int getAmountunits() {
        return amountUnits;
    }

    public void setAmountunits(int amountUnits) {
        this.amountUnits = amountUnits;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getAmountofrecursionpackages() {
        return amountOfRecursionPackages;
    }

    public void setAmountofrecursionpackages(int amountOfRecursionPackages) {
        this.amountOfRecursionPackages = amountOfRecursionPackages;
    }

    public MetaModelGraph_Graph getMetamodelgraph_graph() {
        return metamodelgraph_graph;
    }

    public void setMetamodelgraph_graph(MetaModelGraph_Graph metamodelgraph_graph) {
        this.metamodelgraph_graph = metamodelgraph_graph;
    }

}