





import java.util.List;
import java.util.ArrayList;

public class plsql_type_Datatype extends Type {

    private int range;
    private String name;



    public plsql_type_Datatype(
        int range,        String name    ) {
        super(
        );
        this.range = range;
        this.name = name;
    }


    public int getRange() {
        return range;
    }

    public void setRange(int range) {
        this.range = range;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}