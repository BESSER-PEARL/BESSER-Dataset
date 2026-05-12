





import java.util.List;
import java.util.ArrayList;

public class stext_VariableDefinition extends Variable {

    private boolean readonly;
    private boolean external;
    private String type;





    private stext_Expression stext_expression;


    public stext_VariableDefinition(
        boolean readonly,        boolean external,        String type    ) {
        super(
        );
        this.readonly = readonly;
        this.external = external;
        this.type = type;
    }


    public boolean getReadonly() {
        return readonly;
    }

    public void setReadonly(boolean readonly) {
        this.readonly = readonly;
    }
    public boolean getExternal() {
        return external;
    }

    public void setExternal(boolean external) {
        this.external = external;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public stext_Expression getStext_expression() {
        return stext_expression;
    }

    public void setStext_expression(stext_Expression stext_expression) {
        this.stext_expression = stext_expression;
    }

}