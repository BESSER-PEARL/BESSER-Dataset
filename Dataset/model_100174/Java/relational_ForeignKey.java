





import java.util.List;
import java.util.ArrayList;

public class relational_ForeignKey extends Relationship {

    private String primaryKeyMultiplicity;
    private String foreignKeyMultiplicity;





    private List<relational_Column> relational_columns;




    private relational_UniqueKey relational_uniquekey;




    private relational_UniqueKey relational_uniquekey;




    private relational_Column relational_column;


    public relational_ForeignKey(
        String primaryKeyMultiplicity,        String foreignKeyMultiplicity    ) {
        super(
        );
        this.primaryKeyMultiplicity = primaryKeyMultiplicity;
        this.foreignKeyMultiplicity = foreignKeyMultiplicity;
        this.relational_columns = new ArrayList<>();
    }

    public relational_ForeignKey(
        String primaryKeyMultiplicity,        String foreignKeyMultiplicity        ArrayList<relational_Column> relational_columns    ) {
        this.primaryKeyMultiplicity = primaryKeyMultiplicity;
        this.foreignKeyMultiplicity = foreignKeyMultiplicity;
        this.relational_columns = relational_columns;
    }

    public String getPrimarykeymultiplicity() {
        return primaryKeyMultiplicity;
    }

    public void setPrimarykeymultiplicity(String primaryKeyMultiplicity) {
        this.primaryKeyMultiplicity = primaryKeyMultiplicity;
    }
    public String getForeignkeymultiplicity() {
        return foreignKeyMultiplicity;
    }

    public void setForeignkeymultiplicity(String foreignKeyMultiplicity) {
        this.foreignKeyMultiplicity = foreignKeyMultiplicity;
    }

    public List<relational_Column> getRelational_columns() {
        return relational_columns;
    }

    public void addRelational_column(Relational_column relational_column) {
        this.relational_columns.add(relational_column);
    }
    public relational_UniqueKey getRelational_uniquekey() {
        return relational_uniquekey;
    }

    public void setRelational_uniquekey(relational_UniqueKey relational_uniquekey) {
        this.relational_uniquekey = relational_uniquekey;
    }
    public relational_UniqueKey getRelational_uniquekey() {
        return relational_uniquekey;
    }

    public void setRelational_uniquekey(relational_UniqueKey relational_uniquekey) {
        this.relational_uniquekey = relational_uniquekey;
    }
    public relational_Column getRelational_column() {
        return relational_column;
    }

    public void setRelational_column(relational_Column relational_column) {
        this.relational_column = relational_column;
    }

}