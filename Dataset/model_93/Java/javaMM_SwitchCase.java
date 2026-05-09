





import java.util.List;
import java.util.ArrayList;

public class javaMM_SwitchCase extends Statement {

    private String default;





    private javaMM_Expression javamm_expression;


    public javaMM_SwitchCase(
        String default    ) {
        super(
        );
        this.default = default;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public javaMM_Expression getJavamm_expression() {
        return javamm_expression;
    }

    public void setJavamm_expression(javaMM_Expression javamm_expression) {
        this.javamm_expression = javamm_expression;
    }

}