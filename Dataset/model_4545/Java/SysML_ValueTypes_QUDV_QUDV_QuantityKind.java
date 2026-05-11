





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_QuantityKind extends QuantityKind {

    private boolean isNumberOfEntities;
    private boolean isQuantityOfDimensionOne;



    public SysML_ValueTypes_QUDV_QUDV_QuantityKind(
        boolean isNumberOfEntities,        boolean isQuantityOfDimensionOne    ) {
        super(
        );
        this.isNumberOfEntities = isNumberOfEntities;
        this.isQuantityOfDimensionOne = isQuantityOfDimensionOne;
    }


    public boolean getIsnumberofentities() {
        return isNumberOfEntities;
    }

    public void setIsnumberofentities(boolean isNumberOfEntities) {
        this.isNumberOfEntities = isNumberOfEntities;
    }
    public boolean getIsquantityofdimensionone() {
        return isQuantityOfDimensionOne;
    }

    public void setIsquantityofdimensionone(boolean isQuantityOfDimensionOne) {
        this.isQuantityOfDimensionOne = isQuantityOfDimensionOne;
    }


}