





import java.util.List;
import java.util.ArrayList;

public class database_Column extends NamedElement {

    private String default;
    private int length;
    private String type;
    private String collation;
    private boolean nullable;





    private database_Index database_index;




    private database_Table database_table;


    public database_Column(
        String default,        int length,        String type,        String collation,        boolean nullable    ) {
        super(
        );
        this.default = default;
        this.length = length;
        this.type = type;
        this.collation = collation;
        this.nullable = nullable;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getCollation() {
        return collation;
    }

    public void setCollation(String collation) {
        this.collation = collation;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }

    public database_Index getDatabase_index() {
        return database_index;
    }

    public void setDatabase_index(database_Index database_index) {
        this.database_index = database_index;
    }
    public database_Table getDatabase_table() {
        return database_table;
    }

    public void setDatabase_table(database_Table database_table) {
        this.database_table = database_table;
    }

}