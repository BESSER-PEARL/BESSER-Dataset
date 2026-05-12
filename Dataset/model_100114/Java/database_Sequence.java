





import java.util.List;
import java.util.ArrayList;

public class database_Sequence extends NamedElement {

    private int minValue;
    private int start;
    private int increment;
    private int maxValue;





    private database_TableContainer database_tablecontainer;


    public database_Sequence(
        int minValue,        int start,        int increment,        int maxValue    ) {
        super(
        );
        this.minValue = minValue;
        this.start = start;
        this.increment = increment;
        this.maxValue = maxValue;
    }


    public int getMinvalue() {
        return minValue;
    }

    public void setMinvalue(int minValue) {
        this.minValue = minValue;
    }
    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }
    public int getIncrement() {
        return increment;
    }

    public void setIncrement(int increment) {
        this.increment = increment;
    }
    public int getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(int maxValue) {
        this.maxValue = maxValue;
    }

    public database_TableContainer getDatabase_tablecontainer() {
        return database_tablecontainer;
    }

    public void setDatabase_tablecontainer(database_TableContainer database_tablecontainer) {
        this.database_tablecontainer = database_tablecontainer;
    }

}