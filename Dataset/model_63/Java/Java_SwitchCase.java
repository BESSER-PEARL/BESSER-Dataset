





import java.util.List;
import java.util.ArrayList;

public class Java_SwitchCase extends Statement {

    private boolean default;





    private Java_Expression java_expression;


    public Java_SwitchCase(
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

    public Java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(Java_Expression java_expression) {
        this.java_expression = java_expression;
    }

}