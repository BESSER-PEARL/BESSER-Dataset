





import java.util.List;
import java.util.ArrayList;

public class plsql_type_Datatype extends Type {

    private String name;
    private int range;



    public plsql_type_Datatype(
        String name,        int range    ) {
        super(
        );
        this.name = name;
        this.range = range;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getRange() {
        return range;
    }

    public void setRange(int range) {
        this.range = range;
    }


}