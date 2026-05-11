





import java.util.List;
import java.util.ArrayList;

public class ClockRDL_declarations_FormalToActualMapEntry  {

    private String key;





    private kernel_Declaration kernel_declaration;




    private kernel_Expression kernel_expression;


    public ClockRDL_declarations_FormalToActualMapEntry(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public kernel_Declaration getKernel_declaration() {
        return kernel_declaration;
    }

    public void setKernel_declaration(kernel_Declaration kernel_declaration) {
        this.kernel_declaration = kernel_declaration;
    }
    public kernel_Expression getKernel_expression() {
        return kernel_expression;
    }

    public void setKernel_expression(kernel_Expression kernel_expression) {
        this.kernel_expression = kernel_expression;
    }

}