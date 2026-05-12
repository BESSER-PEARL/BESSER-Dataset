





import java.util.List;
import java.util.ArrayList;

public class RelationalDBContent_TupleElement  {

    private String value;





    private Tuple tuple;


    public RelationalDBContent_TupleElement(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public Tuple getTuple() {
        return tuple;
    }

    public void setTuple(Tuple tuple) {
        this.tuple = tuple;
    }

}