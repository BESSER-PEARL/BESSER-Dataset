





import java.util.List;
import java.util.ArrayList;

public class website_EncapsulatedFeature extends ViewFeature {

    private String columnName;
    private String displayLabel;
    private String alias;



    public website_EncapsulatedFeature(
        String columnName,        String displayLabel,        String alias    ) {
        super(
        );
        this.columnName = columnName;
        this.displayLabel = displayLabel;
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
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }


}