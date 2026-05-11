





import java.util.List;
import java.util.ArrayList;

public class workflow_Constant extends Expression {

    private String asBoolean;
    private String asReal;
    private String asInteger;
    private String asString;



    public workflow_Constant(
        String asBoolean,        String asReal,        String asInteger,        String asString    ) {
        super(
        );
        this.asBoolean = asBoolean;
        this.asReal = asReal;
        this.asInteger = asInteger;
        this.asString = asString;
    }


    public String getAsboolean() {
        return asBoolean;
    }

    public void setAsboolean(String asBoolean) {
        this.asBoolean = asBoolean;
    }
    public String getAsreal() {
        return asReal;
    }

    public void setAsreal(String asReal) {
        this.asReal = asReal;
    }
    public String getAsinteger() {
        return asInteger;
    }

    public void setAsinteger(String asInteger) {
        this.asInteger = asInteger;
    }
    public String getAsstring() {
        return asString;
    }

    public void setAsstring(String asString) {
        this.asString = asString;
    }


}