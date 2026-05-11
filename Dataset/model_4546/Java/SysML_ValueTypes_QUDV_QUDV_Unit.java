





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_Unit extends Unit {

    private boolean isUnitForQuantityOfDimensionOne;
    private boolean isUnitCountOfEntities;



    public SysML_ValueTypes_QUDV_QUDV_Unit(
        boolean isUnitForQuantityOfDimensionOne,        boolean isUnitCountOfEntities    ) {
        super(
        );
        this.isUnitForQuantityOfDimensionOne = isUnitForQuantityOfDimensionOne;
        this.isUnitCountOfEntities = isUnitCountOfEntities;
    }


    public boolean getIsunitforquantityofdimensionone() {
        return isUnitForQuantityOfDimensionOne;
    }

    public void setIsunitforquantityofdimensionone(boolean isUnitForQuantityOfDimensionOne) {
        this.isUnitForQuantityOfDimensionOne = isUnitForQuantityOfDimensionOne;
    }
    public boolean getIsunitcountofentities() {
        return isUnitCountOfEntities;
    }

    public void setIsunitcountofentities(boolean isUnitCountOfEntities) {
        this.isUnitCountOfEntities = isUnitCountOfEntities;
    }


}