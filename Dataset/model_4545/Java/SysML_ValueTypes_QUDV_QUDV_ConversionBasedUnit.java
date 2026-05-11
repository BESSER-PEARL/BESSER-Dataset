





import java.util.List;
import java.util.ArrayList;

public class SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit extends Unit {

    private boolean isInvertible;



    public SysML_ValueTypes_QUDV_QUDV_ConversionBasedUnit(
        boolean isInvertible    ) {
        super(
        );
        this.isInvertible = isInvertible;
    }


    public boolean getIsinvertible() {
        return isInvertible;
    }

    public void setIsinvertible(boolean isInvertible) {
        this.isInvertible = isInvertible;
    }


}