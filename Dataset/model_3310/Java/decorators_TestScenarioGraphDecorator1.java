





import java.util.List;
import java.util.ArrayList;

public class decorators_TestScenarioGraphDecorator1 extends GraphDecorator {

    private float doubleValue;
    private int intValue;
    private boolean booleanValue;
    private String stringValue;



    public decorators_TestScenarioGraphDecorator1(
        float doubleValue,        int intValue,        boolean booleanValue,        String stringValue    ) {
        super(
        );
        this.doubleValue = doubleValue;
        this.intValue = intValue;
        this.booleanValue = booleanValue;
        this.stringValue = stringValue;
    }


    public float getDoublevalue() {
        return doubleValue;
    }

    public void setDoublevalue(float doubleValue) {
        this.doubleValue = doubleValue;
    }
    public int getIntvalue() {
        return intValue;
    }

    public void setIntvalue(int intValue) {
        this.intValue = intValue;
    }
    public boolean getBooleanvalue() {
        return booleanValue;
    }

    public void setBooleanvalue(boolean booleanValue) {
        this.booleanValue = booleanValue;
    }
    public String getStringvalue() {
        return stringValue;
    }

    public void setStringvalue(String stringValue) {
        this.stringValue = stringValue;
    }


}