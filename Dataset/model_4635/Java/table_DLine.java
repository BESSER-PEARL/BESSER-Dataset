





import java.util.List;
import java.util.ArrayList;

public class table_DLine extends LineContainer, DTableElement {

    private boolean collapsed;
    private String label;
    private boolean visible;





    private LineMapping linemapping;




    private List<table_DCell> table_dcells;




    private table_DCell table_dcell;




    private List<table_DCell> table_dcells;


    public table_DLine(
        boolean collapsed,        String label,        boolean visible    ) {
        super(
        );
        this.collapsed = collapsed;
        this.label = label;
        this.visible = visible;
        this.table_dcells = new ArrayList<>();
        this.table_dcells = new ArrayList<>();
    }

    public table_DLine(
        boolean collapsed,        String label,        boolean visible        ArrayList<table_DCell> table_dcells,        ArrayList<table_DCell> table_dcells    ) {
        this.collapsed = collapsed;
        this.label = label;
        this.visible = visible;
        this.table_dcells = table_dcells;
        this.table_dcells = table_dcells;
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
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }

    public LineMapping getLinemapping() {
        return linemapping;
    }

    public void setLinemapping(LineMapping linemapping) {
        this.linemapping = linemapping;
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
    public List<table_DCell> getTable_dcells() {
        return table_dcells;
    }

    public void addTable_dcell(Table_dcell table_dcell) {
        this.table_dcells.add(table_dcell);
    }

}