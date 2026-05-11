





import java.util.List;
import java.util.ArrayList;

public class plsql_type_IndirectType extends Type {

    private String identifier;
    private boolean type;
    private int range;
    private boolean rowtype;



    public plsql_type_IndirectType(
        String identifier,        boolean type,        int range,        boolean rowtype    ) {
        super(
        );
        this.identifier = identifier;
        this.type = type;
        this.range = range;
        this.rowtype = rowtype;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public boolean getType() {
        return type;
    }

    public void setType(boolean type) {
        this.type = type;
    }
    public int getRange() {
        return range;
    }

    public void setRange(int range) {
        this.range = range;
    }
    public boolean getRowtype() {
        return rowtype;
    }

    public void setRowtype(boolean rowtype) {
        this.rowtype = rowtype;
    }


}