





import java.util.List;
import java.util.ArrayList;

public class table_DColumn extends DTableElement {

    private boolean visible;
    private int width;
    private String label;





    private List<table_DCell> table_dcells;




    private table_DCell table_dcell;




    private List<table_DCell> table_dcells;


    public table_DColumn(
        boolean visible,        int width,        String label    ) {
        super(
        );
        this.visible = visible;
        this.width = width;
        this.label = label;
        this.table_dcells = new ArrayList<>();
        this.table_dcells = new ArrayList<>();
    }

    public table_DColumn(
        boolean visible,        int width,        String label        ArrayList<table_DCell> table_dcells,        ArrayList<table_DCell> table_dcells    ) {
        this.visible = visible;
        this.width = width;
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
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
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