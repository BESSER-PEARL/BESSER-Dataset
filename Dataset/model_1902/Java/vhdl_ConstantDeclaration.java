





import java.util.List;
import java.util.ArrayList;

public class vhdl_ConstantDeclaration extends package_declarative_item, BlockDeclarativeItem {






    private vhdl_Expression vhdl_expression;


    public vhdl_ConstantDeclaration(
    ) {
        super(
        );
    }



    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }

}