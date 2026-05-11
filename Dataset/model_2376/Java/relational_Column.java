





import java.util.List;
import java.util.ArrayList;

public class relational_Column extends TypedElement {

    private String defaultValue;
    private String srid;
    private int length;
    private boolean nullable;





    private relational_Table relational_table;




    private relational_Table relational_table;


    public relational_Column(
        String defaultValue,        String srid,        int length,        boolean nullable    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.srid = srid;
        this.length = length;
        this.nullable = nullable;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getSrid() {
        return srid;
    }

    public void setSrid(String srid) {
        this.srid = srid;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
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