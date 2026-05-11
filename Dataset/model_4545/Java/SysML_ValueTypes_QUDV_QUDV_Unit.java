





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_Unit extends Unit {

    private boolean isUnitCountOfEntities;
    private boolean isUnitForQuantityOfDimensionOne;



    public SysML_ValueTypes_QUDV_QUDV_Unit(
        boolean isUnitCountOfEntities,        boolean isUnitForQuantityOfDimensionOne    ) {
        super(
        );
        this.isUnitCountOfEntities = isUnitCountOfEntities;
        this.isUnitForQuantityOfDimensionOne = isUnitForQuantityOfDimensionOne;
    }


    public boolean getIsunitcountofentities() {
        return isUnitCountOfEntities;
    }

    public void setIsunitcountofentities(boolean isUnitCountOfEntities) {
        this.isUnitCountOfEntities = isUnitCountOfEntities;
    }
    public boolean getIsunitforquantityofdimensionone() {
        return isUnitForQuantityOfDimensionOne;
    }

    public void setIsunitforquantityofdimensionone(boolean isUnitForQuantityOfDimensionOne) {
        this.isUnitForQuantityOfDimensionOne = isUnitForQuantityOfDimensionOne;
    }


}