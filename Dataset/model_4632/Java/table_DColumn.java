





import java.util.List;
import java.util.ArrayList;

public class table_DColumn extends DTableElement {

    private int width;
    private boolean visible;
    private String label;





    private table_DCell table_dcell;




    private table_DTable table_dtable;




    private table_DTable table_dtable;




    private List<table_DCell> table_dcells;




    private List<table_DCell> table_dcells;


    public table_DColumn(
        int width,        boolean visible,        String label    ) {
        super(
        );
        this.width = width;
        this.visible = visible;
        this.label = label;
        this.table_dcells = new ArrayList<>();
        this.table_dcells = new ArrayList<>();
    }

    public table_DColumn(
        int width,        boolean visible,        String label        ArrayList<table_DCell> table_dcells,        ArrayList<table_DCell> table_dcells    ) {
        this.width = width;
        this.visible = visible;
        this.label = label;
        this.table_dcells = table_dcells;
        this.table_dcells = table_dcells;
    }

    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
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

    public table_DCell getTable_dcell() {
        return table_dcell;
    }

    public void setTable_dcell(table_DCell table_dcell) {
        this.table_dcell = table_dcell;
    }
    public table_DTable getTable_dtable() {
        return table_dtable;
    }

    public void setTable_dtable(table_DTable table_dtable) {
        this.table_dtable = table_dtable;
    }
    public table_DTable getTable_dtable() {
        return table_dtable;
    }

    public void setTable_dtable(table_DTable table_dtable) {
        this.table_dtable = table_dtable;
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

}