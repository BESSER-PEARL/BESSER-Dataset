





import java.util.List;
import java.util.ArrayList;

public class JDTAST_SwitchCase extends Statement {

    private String default;





    private JDTAST_Expression jdtast_expression;


    public JDTAST_SwitchCase(
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

    public JDTAST_Expression getJdtast_expression() {
        return jdtast_expression;
    }

    public void setJdtast_expression(JDTAST_Expression jdtast_expression) {
        this.jdtast_expression = jdtast_expression;
    }

}