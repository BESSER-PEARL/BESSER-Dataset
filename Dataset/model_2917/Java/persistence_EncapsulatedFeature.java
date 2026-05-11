





import java.util.List;
import java.util.ArrayList;

public class persistence_EncapsulatedFeature extends ViewFeature {

    private String alias;
    private String columnName;
    private String displayLabel;



    public persistence_EncapsulatedFeature(
        String alias,        String columnName,        String displayLabel    ) {
        super(
        );
        this.alias = alias;
        this.columnName = columnName;
        this.displayLabel = displayLabel;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getDisplaylabel() {
        return displayLabel;
    }

    public void setDisplaylabel(String displayLabel) {
        this.displayLabel = displayLabel;
    }


}