





import java.util.List;
import java.util.ArrayList;

public class table_DColumn extends DTableElement {

    private String label;
    private boolean visible;
    private int width;





    private List<table_DCell> table_dcells;




    private table_DTable table_dtable;




    private table_DCell table_dcell;




    private List<table_DCell> table_dcells;




    private table_DTable table_dtable;


    public table_DColumn(
        String label,        boolean visible,        int width    ) {
        super(
        );
        this.label = label;
        this.visible = visible;
        this.width = width;
        this.table_dcells = new ArrayList<>();
        this.table_dcells = new ArrayList<>();
    }

    public table_DColumn(
        String label,        boolean visible,        int width        ArrayList<table_DCell> table_dcells,        ArrayList<table_DCell> table_dcells    ) {
        this.label = label;
        this.visible = visible;
        this.width = width;
        this.table_dcells = table_dcells;
        this.table_dcells = table_dcells;
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
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public List<table_DCell> getTable_dcells() {
        return table_dcells;
    }

    public void addTable_dcell(Table_dcell table_dcell) {
        this.table_dcells.add(table_dcell);
    }
    public table_DTable getTable_dtable() {
        return table_dtable;
    }

    public void setTable_dtable(table_DTable table_dtable) {
        this.table_dtable = table_dtable;
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
    public table_DTable getTable_dtable() {
        return table_dtable;
    }

    public void setTable_dtable(table_DTable table_dtable) {
        this.table_dtable = table_dtable;
    }

}