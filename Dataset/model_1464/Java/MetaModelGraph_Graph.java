





import java.util.List;
import java.util.ArrayList;

public class MetaModelGraph_Graph  {

    private int amountEClasses;
    private int amountConcreteEClass;
    private int amountAbstractEClasses;



    public MetaModelGraph_Graph(
        int amountEClasses,        int amountConcreteEClass,        int amountAbstractEClasses    ) {
        this.amountEClasses = amountEClasses;
        this.amountConcreteEClass = amountConcreteEClass;
        this.amountAbstractEClasses = amountAbstractEClasses;
    }


    public int getAmounteclasses() {
        return amountEClasses;
    }

    public void setAmounteclasses(int amountEClasses) {
        this.amountEClasses = amountEClasses;
    }
    public int getAmountconcreteeclass() {
        return amountConcreteEClass;
    }

    public void setAmountconcreteeclass(int amountConcreteEClass) {
        this.amountConcreteEClass = amountConcreteEClass;
    }
    public int getAmountabstracteclasses() {
        return amountAbstractEClasses;
    }

    public void setAmountabstracteclasses(int amountAbstractEClasses) {
        this.amountAbstractEClasses = amountAbstractEClasses;
    }


}