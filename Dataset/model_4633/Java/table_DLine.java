





import java.util.List;
import java.util.ArrayList;

public class table_DLine extends DTableElement, LineContainer {

    private boolean visible;
    private boolean collapsed;
    private String label;





    private table_LineContainer table_linecontainer;




    private List<table_DCell> table_dcells;




    private table_LineContainer table_linecontainer;




    private table_DCell table_dcell;




    private List<table_DCell> table_dcells;


    public table_DLine(
        boolean visible,        boolean collapsed,        String label    ) {
        super(
        );
        this.visible = visible;
        this.collapsed = collapsed;
        this.label = label;
        this.table_dcells = new ArrayList<>();
        this.table_dcells = new ArrayList<>();
    }

    public table_DLine(
        boolean visible,        boolean collapsed,        String label        ArrayList<table_DCell> table_dcells,        ArrayList<table_DCell> table_dcells    ) {
        this.visible = visible;
        this.collapsed = collapsed;
        this.label = label;
        this.table_dcells = table_dcells;
        this.table_dcells = table_dcells;
    }

    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public boolean getCollapsed() {
        return collapsed;
    }

    public void setCollapsed(boolean collapsed) {
        this.collapsed = collapsed;
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
    public List<table_DCell> getTable_dcells() {
        return table_dcells;
    }

    public void addTable_dcell(Table_dcell table_dcell) {
        this.table_dcells.add(table_dcell);
    }
    public table_LineContainer getTable_linecontainer() {
        return table_linecontainer;
    }

    public void setTable_linecontainer(table_LineContainer table_linecontainer) {
        this.table_linecontainer = table_linecontainer;
    }
    public table_DCell getTable_dcell() {
        return table_dcell;
    }

    public void setTable_dcell(table_DCell table_dcell) {
        this.table_dcell = table_dcell;
    }
    public List<table_DCell> getTable_dcells() {
        return table_dcells;
    }

    public void addTable_dcell(Table_dcell table_dcell) {
        this.table_dcells.add(table_dcell);
    }

}