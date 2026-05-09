





import java.util.List;
import java.util.ArrayList;

public class java_SwitchCase extends Statement {

    private boolean default;





    private java_Expression java_expression;


    public java_SwitchCase(
        boolean default    ) {
        super(
        );
        this.default = default;
    }


    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }

    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }

}