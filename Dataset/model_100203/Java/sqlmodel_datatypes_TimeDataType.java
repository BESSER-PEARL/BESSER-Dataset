





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_TimeDataType extends PredefinedDataType {

    private boolean timeZone;
    private int fractionalSecondsPrecision;



    public sqlmodel_datatypes_TimeDataType(
        boolean timeZone,        int fractionalSecondsPrecision    ) {
        super(
        );
        this.timeZone = timeZone;
        this.fractionalSecondsPrecision = fractionalSecondsPrecision;
    }


    public boolean getTimezone() {
        return timeZone;
    }

    public void setTimezone(boolean timeZone) {
        this.timeZone = timeZone;
    }
    public int getFractionalsecondsprecision() {
        return fractionalSecondsPrecision;
    }

    public void setFractionalsecondsprecision(int fractionalSecondsPrecision) {
        this.fractionalSecondsPrecision = fractionalSecondsPrecision;
    }


}