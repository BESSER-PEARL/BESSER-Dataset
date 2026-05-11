





import java.util.List;
import java.util.ArrayList;

public class genericsql_Field extends NamedElement {

    private String specificType;
    private boolean notNull;
    private int size;
    private boolean autoIcrement;
    private String type;
    private String defaultValue;
    private boolean unique;





    private genericsql_Table genericsql_table;




    private genericsql_Table genericsql_table;




    private genericsql_PrimaryKey genericsql_primarykey;




    private genericsql_ForeignKey genericsql_foreignkey;


    public genericsql_Field(
        String specificType,        boolean notNull,        int size,        boolean autoIcrement,        String type,        String defaultValue,        boolean unique    ) {
        super(
        );
        this.specificType = specificType;
        this.notNull = notNull;
        this.size = size;
        this.autoIcrement = autoIcrement;
        this.type = type;
        this.defaultValue = defaultValue;
        this.unique = unique;
    }


    public String getSpecifictype() {
        return specificType;
    }

    public void setSpecifictype(String specificType) {
        this.specificType = specificType;
    }
    public boolean getNotnull() {
        return notNull;
    }

    public void setNotnull(boolean notNull) {
        this.notNull = notNull;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public boolean getAutoicrement() {
        return autoIcrement;
    }

    public void setAutoicrement(boolean autoIcrement) {
        this.autoIcrement = autoIcrement;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }

    public genericsql_Table getGenericsql_table() {
        return genericsql_table;
    }

    public void setGenericsql_table(genericsql_Table genericsql_table) {
        this.genericsql_table = genericsql_table;
    }
    public genericsql_Table getGenericsql_table() {
        return genericsql_table;
    }

    public void setGenericsql_table(genericsql_Table genericsql_table) {
        this.genericsql_table = genericsql_table;
    }
    public genericsql_PrimaryKey getGenericsql_primarykey() {
        return genericsql_primarykey;
    }

    public void setGenericsql_primarykey(genericsql_PrimaryKey genericsql_primarykey) {
        this.genericsql_primarykey = genericsql_primarykey;
    }
    public genericsql_ForeignKey getGenericsql_foreignkey() {
        return genericsql_foreignkey;
    }

    public void setGenericsql_foreignkey(genericsql_ForeignKey genericsql_foreignkey) {
        this.genericsql_foreignkey = genericsql_foreignkey;
    }

}