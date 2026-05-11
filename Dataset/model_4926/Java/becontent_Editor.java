





import java.util.List;
import java.util.ArrayList;

public class becontent_Editor extends NotStructuredElement {

    private boolean isMandatory;
    private String label;
    private String name;
    private int rows;
    private int columns;



    public becontent_Editor(
        boolean isMandatory,        String label,        String name,        int rows,        int columns    ) {
        super(
        );
        this.isMandatory = isMandatory;
        this.label = label;
        this.name = name;
        this.rows = rows;
        this.columns = columns;
    }


    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getRows() {
        return rows;
    }

    public void setRows(int rows) {
        this.rows = rows;
    }
    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }


}