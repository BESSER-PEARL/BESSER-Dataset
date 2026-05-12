





import java.util.List;
import java.util.ArrayList;

public class table_LineContainer extends DSemanticDecorator {






    private List<table_DLine> table_dlines;




    private table_DLine table_dline;


    public table_LineContainer(
    ) {
        super(
        );
        this.table_dlines = new ArrayList<>();
    }

    public table_LineContainer(
        ArrayList<table_DLine> table_dlines    ) {
        this.table_dlines = table_dlines;
    }


    public List<table_DLine> getTable_dlines() {
        return table_dlines;
    }

    public void addTable_dline(Table_dline table_dline) {
        this.table_dlines.add(table_dline);
    }
    public table_DLine getTable_dline() {
        return table_dline;
    }

    public void setTable_dline(table_DLine table_dline) {
        this.table_dline = table_dline;
    }

}