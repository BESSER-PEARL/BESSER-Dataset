





import java.util.List;
import java.util.ArrayList;

public class workflow_Constant extends Expression {

    private String asBoolean;
    private String asString;
    private String asInteger;
    private String asReal;



    public workflow_Constant(
        String asBoolean,        String asString,        String asInteger,        String asReal    ) {
        super(
        );
        this.asBoolean = asBoolean;
        this.asString = asString;
        this.asInteger = asInteger;
        this.asReal = asReal;
    }


    public String getAsboolean() {
        return asBoolean;
    }

    public void setAsboolean(String asBoolean) {
        this.asBoolean = asBoolean;
    }
    public String getAsstring() {
        return asString;
    }

    public void setAsstring(String asString) {
        this.asString = asString;
    }
    public String getAsinteger() {
        return asInteger;
    }

    public void setAsinteger(String asInteger) {
        this.asInteger = asInteger;
    }
    public String getAsreal() {
        return asReal;
    }

    public void setAsreal(String asReal) {
        this.asReal = asReal;
    }


}