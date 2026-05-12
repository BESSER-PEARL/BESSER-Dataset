





import java.util.List;
import java.util.ArrayList;

public class plsql_type_IndirectType extends Type {

    private String identifier;
    private int range;
    private boolean type;
    private boolean rowtype;



    public plsql_type_IndirectType(
        String identifier,        int range,        boolean type,        boolean rowtype    ) {
        super(
        );
        this.identifier = identifier;
        this.range = range;
        this.type = type;
        this.rowtype = rowtype;
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
    public boolean getType() {
        return type;
    }

    public void setType(boolean type) {
        this.type = type;
    }
    public boolean getRowtype() {
        return rowtype;
    }

    public void setRowtype(boolean rowtype) {
        this.rowtype = rowtype;
    }


}