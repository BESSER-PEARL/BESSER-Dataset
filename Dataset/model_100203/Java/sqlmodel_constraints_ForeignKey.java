





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_constraints_ForeignKey extends ReferenceConstraint {

    private String onUpdate;
    private String onDelete;
    private String match;





    private Index index;




    private List<Column> columns;




    private BaseTable basetable;


    public sqlmodel_constraints_ForeignKey(
        String onUpdate,        String onDelete,        String match    ) {
        super(
        );
        this.onUpdate = onUpdate;
        this.onDelete = onDelete;
        this.match = match;
        this.columns = new ArrayList<>();
    }

    public sqlmodel_constraints_ForeignKey(
        String onUpdate,        String onDelete,        String match        ArrayList<Column> columns    ) {
        this.onUpdate = onUpdate;
        this.onDelete = onDelete;
        this.match = match;
        this.columns = columns;
    }

    public String getOnupdate() {
        return onUpdate;
    }

    public void setOnupdate(String onUpdate) {
        this.onUpdate = onUpdate;
    }
    public String getOndelete() {
        return onDelete;
    }

    public void setOndelete(String onDelete) {
        this.onDelete = onDelete;
    }
    public String getMatch() {
        return match;
    }

    public void setMatch(String match) {
        this.match = match;
    }

    public Index getIndex() {
        return index;
    }

    public void setIndex(Index index) {
        this.index = index;
    }
    public List<Column> getColumns() {
        return columns;
    }

    public void addColumn(Column column) {
        this.columns.add(column);
    }
    public BaseTable getBasetable() {
        return basetable;
    }

    public void setBasetable(BaseTable basetable) {
        this.basetable = basetable;
    }

}