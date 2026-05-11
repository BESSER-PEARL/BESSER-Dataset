





import java.util.List;
import java.util.ArrayList;

public class becontent_Textarea extends NotStructuredElement {

    private int rows;
    private String name;
    private String label;
    private int columns;
    private boolean isMandatory;



    public becontent_Textarea(
        int rows,        String name,        String label,        int columns,        boolean isMandatory    ) {
        super(
        );
        this.rows = rows;
        this.name = name;
        this.label = label;
        this.columns = columns;
        this.isMandatory = isMandatory;
    }


    public int getRows() {
        return rows;
    }

    public void setRows(int rows) {
        this.rows = rows;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }
    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }


}