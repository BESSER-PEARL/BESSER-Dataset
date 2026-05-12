





import java.util.List;
import java.util.ArrayList;

public class jPQL_ParameterExpression extends Variable {

    private String name;
    private int index;



    public jPQL_ParameterExpression(
        String name,        int index    ) {
        super(
        );
        this.name = name;
        this.index = index;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }


}