





import java.util.List;
import java.util.ArrayList;

public class adb_DeltaConstraint extends ScalarConstraint {






    private adb_RangeConstraint adb_rangeconstraint;




    private adb_SimpleExpression adb_simpleexpression;


    public adb_DeltaConstraint(
    ) {
        super(
        );
    }



    public adb_RangeConstraint getAdb_rangeconstraint() {
        return adb_rangeconstraint;
    }

    public void setAdb_rangeconstraint(adb_RangeConstraint adb_rangeconstraint) {
        this.adb_rangeconstraint = adb_rangeconstraint;
    }
    public adb_SimpleExpression getAdb_simpleexpression() {
        return adb_simpleexpression;
    }

    public void setAdb_simpleexpression(adb_SimpleExpression adb_simpleexpression) {
        this.adb_simpleexpression = adb_simpleexpression;
    }

}