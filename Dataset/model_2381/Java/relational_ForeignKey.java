





import java.util.List;
import java.util.ArrayList;

public class relational_ForeignKey extends ReferenceConstraint {

    private String onDelete;
    private String onUpdate;





    private List<relational_Column> relational_columns;




    private relational_Column relational_column;


    public relational_ForeignKey(
        String onDelete,        String onUpdate    ) {
        super(
        );
        this.onDelete = onDelete;
        this.onUpdate = onUpdate;
        this.relational_columns = new ArrayList<>();
    }

    public relational_ForeignKey(
        String onDelete,        String onUpdate        ArrayList<relational_Column> relational_columns    ) {
        this.onDelete = onDelete;
        this.onUpdate = onUpdate;
        this.relational_columns = relational_columns;
    }

    public String getOndelete() {
        return onDelete;
    }

    public void setOndelete(String onDelete) {
        this.onDelete = onDelete;
    }
    public String getOnupdate() {
        return onUpdate;
    }

    public void setOnupdate(String onUpdate) {
        this.onUpdate = onUpdate;
    }

    public List<relational_Column> getRelational_columns() {
        return relational_columns;
    }

    public void addRelational_column(Relational_column relational_column) {
        this.relational_columns.add(relational_column);
    }
    public relational_Column getRelational_column() {
        return relational_column;
    }

    public void setRelational_column(relational_Column relational_column) {
        this.relational_column = relational_column;
    }

}