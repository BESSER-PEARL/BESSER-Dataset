





import java.util.List;
import java.util.ArrayList;

public class rcl_VarRef extends StringValue, Statement, NumberValue, BooleanValue {

    private String name;



    public rcl_VarRef(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}