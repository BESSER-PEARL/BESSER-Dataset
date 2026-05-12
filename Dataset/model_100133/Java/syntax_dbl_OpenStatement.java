





import java.util.List;
import java.util.ArrayList;

public class syntax_dbl_OpenStatement extends BindingStatement {

    private String cursor;
    private String usingType;
    private String using;



    public syntax_dbl_OpenStatement(
        String cursor,        String usingType,        String using    ) {
        super(
        );
        this.cursor = cursor;
        this.usingType = usingType;
        this.using = using;
    }


    public String getCursor() {
        return cursor;
    }

    public void setCursor(String cursor) {
        this.cursor = cursor;
    }
    public String getUsingtype() {
        return usingType;
    }

    public void setUsingtype(String usingType) {
        this.usingType = usingType;
    }
    public String getUsing() {
        return using;
    }

    public void setUsing(String using) {
        this.using = using;
    }


}