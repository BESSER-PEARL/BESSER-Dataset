





import java.util.List;
import java.util.ArrayList;

public class vhdl_SignalDeclaration extends package_declarative_item, BlockDeclarativeItem {

    private String kind;





    private vhdl_Expression vhdl_expression;


    public vhdl_SignalDeclaration(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public vhdl_Expression getVhdl_expression() {
        return vhdl_expression;
    }

    public void setVhdl_expression(vhdl_Expression vhdl_expression) {
        this.vhdl_expression = vhdl_expression;
    }

}