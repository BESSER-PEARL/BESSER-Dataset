





import java.util.List;
import java.util.ArrayList;

public class relational_Column extends TypedElement {

    private int length;
    private String defaultValue;
    private boolean nullable;





    private relational_ForeignKey relational_foreignkey;




    private List<relational_ForeignKey> relational_foreignkeys;




    private relational_Table relational_table;




    private relational_Table relational_table;


    public relational_Column(
        int length,        String defaultValue,        boolean nullable    ) {
        super(
        );
        this.length = length;
        this.defaultValue = defaultValue;
        this.nullable = nullable;
        this.relational_foreignkeys = new ArrayList<>();
    }

    public relational_Column(
        int length,        String defaultValue,        boolean nullable        ArrayList<relational_ForeignKey> relational_foreignkeys    ) {
        this.length = length;
        this.defaultValue = defaultValue;
        this.nullable = nullable;
        this.relational_foreignkeys = relational_foreignkeys;
    }

    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }

    public relational_ForeignKey getRelational_foreignkey() {
        return relational_foreignkey;
    }

    public void setRelational_foreignkey(relational_ForeignKey relational_foreignkey) {
        this.relational_foreignkey = relational_foreignkey;
    }
    public List<relational_ForeignKey> getRelational_foreignkeys() {
        return relational_foreignkeys;
    }

    public void addRelational_foreignkey(Relational_foreignkey relational_foreignkey) {
        this.relational_foreignkeys.add(relational_foreignkey);
    }
    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }
    public relational_Table getRelational_table() {
        return relational_table;
    }

    public void setRelational_table(relational_Table relational_table) {
        this.relational_table = relational_table;
    }

}