





import java.util.List;
import java.util.ArrayList;

public class feature_AttributeValue extends AttributeOperand {

    private int int;
    private String name;



    public feature_AttributeValue(
        int int,        String name    ) {
        super(
        );
        this.int = int;
        this.name = name;
    }


    public int getInt() {
        return int;
    }

    public void setInt(int int) {
        this.int = int;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}