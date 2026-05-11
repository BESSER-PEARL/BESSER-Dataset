





import java.util.List;
import java.util.ArrayList;

public class persistence_EncapsulatedFeature extends ViewFeature {

    private String displayLabel;
    private String alias;
    private String columnName;



    public persistence_EncapsulatedFeature(
        String displayLabel,        String alias,        String columnName    ) {
        super(
        );
        this.displayLabel = displayLabel;
        this.alias = alias;
        this.columnName = columnName;
    }


    public String getDisplaylabel() {
        return displayLabel;
    }

    public void setDisplaylabel(String displayLabel) {
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


}