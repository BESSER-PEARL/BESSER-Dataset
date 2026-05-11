





import java.util.List;
import java.util.ArrayList;

public class go_BasicType  {

    private String int;
    private String float;
    private String string;
    private String boolean;





    private go_ArrayType go_arraytype;


    public go_BasicType(
        String int,        String float,        String string,        String boolean    ) {
        this.int = int;
        this.float = float;
        this.string = string;
        this.boolean = boolean;
    }


    public String getInt() {
        return int;
    }

    public void setInt(String int) {
        this.int = int;
    }
    public String getFloat() {
        return float;
    }

    public void setFloat(String float) {
        this.float = float;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public String getBoolean() {
        return boolean;
    }

    public void setBoolean(String boolean) {
        this.boolean = boolean;
    }

    public go_ArrayType getGo_arraytype() {
        return go_arraytype;
    }

    public void setGo_arraytype(go_ArrayType go_arraytype) {
        this.go_arraytype = go_arraytype;
    }

}