





import java.util.List;
import java.util.ArrayList;

public class stext_VariableDefinition extends Property, Variable {

    private boolean readonly;
    private boolean external;





    private stext_Expression stext_expression;


    public stext_VariableDefinition(
        boolean readonly,        boolean external    ) {
        super(
        );
        this.readonly = readonly;
        this.external = external;
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

    public stext_Expression getStext_expression() {
        return stext_expression;
    }

    public void setStext_expression(stext_Expression stext_expression) {
        this.stext_expression = stext_expression;
    }

}