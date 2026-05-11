





import java.util.List;
import java.util.ArrayList;

public class plsql_type_IndirectType extends Type {

    private boolean rowtype;
    private boolean type;
    private String identifier;
    private int range;



    public plsql_type_IndirectType(
        boolean rowtype,        boolean type,        String identifier,        int range    ) {
        super(
        );
        this.rowtype = rowtype;
        this.type = type;
        this.identifier = identifier;
        this.range = range;
    }


    public boolean getRowtype() {
        return rowtype;
    }

    public void setRowtype(boolean rowtype) {
        this.rowtype = rowtype;
    }
    public boolean getType() {
        return type;
    }

    public void setType(boolean type) {
        this.type = type;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public int getRange() {
        return range;
    }

    public void setRange(int range) {
        this.range = range;
    }


}