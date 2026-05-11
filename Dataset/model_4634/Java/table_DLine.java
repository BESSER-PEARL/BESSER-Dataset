





import java.util.List;
import java.util.ArrayList;

public class table_DLine extends DTableElement, LineContainer {

    private boolean collapsed;
    private boolean visible;
    private String label;





    private table_LineContainer table_linecontainer;




    private table_LineContainer table_linecontainer;




    private List<table_DCell> table_dcells;




    private List<table_DCell> table_dcells;




    private table_DCell table_dcell;


    public table_DLine(
        boolean collapsed,        boolean visible,        String label    ) {
        super(
        );
        this.collapsed = collapsed;
        this.visible = visible;
        this.label = label;
        this.table_dcells = new ArrayList<>();
        this.table_dcells = new ArrayList<>();
    }

    public table_DLine(
        boolean collapsed,        boolean visible,        String label        ArrayList<table_DCell> table_dcells,        ArrayList<table_DCell> table_dcells    ) {
        this.collapsed = collapsed;
        this.visible = visible;
        this.label = label;
        this.table_dcells = table_dcells;
        this.table_dcells = table_dcells;
    }

    public boolean getCollapsed() {
        return collapsed;
    }

    public void setCollapsed(boolean collapsed) {
        this.collapsed = collapsed;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public table_LineContainer getTable_linecontainer() {
        return table_linecontainer;
    }

    public void setTable_linecontainer(table_LineContainer table_linecontainer) {
        this.table_linecontainer = table_linecontainer;
    }
    public table_LineContainer getTable_linecontainer() {
        return table_linecontainer;
    }

    public void setTable_linecontainer(table_LineContainer table_linecontainer) {
        this.table_linecontainer = table_linecontainer;
    }
    public List<table_DCell> getTable_dcells() {
        return table_dcells;
    }

    public void addTable_dcell(Table_dcell table_dcell) {
        this.table_dcells.add(table_dcell);
    }
    public List<table_DCell> getTable_dcells() {
        return table_dcells;
    }

    public void addTable_dcell(Table_dcell table_dcell) {
        this.table_dcells.add(table_dcell);
    }
    public table_DCell getTable_dcell() {
        return table_dcell;
    }

    public void setTable_dcell(table_DCell table_dcell) {
        this.table_dcell = table_dcell;
    }

}