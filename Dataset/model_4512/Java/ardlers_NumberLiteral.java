





import java.util.List;
import java.util.ArrayList;

public class ardlers_NumberLiteral extends Value {

    private int int;
    private String float;



    public ardlers_NumberLiteral(
        int int,        String float    ) {
        super(
        );
        this.int = int;
        this.float = float;
    }


    public int getInt() {
        return int;
    }

    public void setInt(int int) {
        this.int = int;
    }
    public String getFloat() {
        return float;
    }

    public void setFloat(String float) {
        this.float = float;
    }


}