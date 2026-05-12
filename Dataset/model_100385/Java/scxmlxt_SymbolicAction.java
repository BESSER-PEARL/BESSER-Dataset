





import java.util.List;
import java.util.ArrayList;

public class scxmlxt_SymbolicAction extends Action {

    private String name;





    private scxmlxt_Expression scxmlxt_expression;


    public scxmlxt_SymbolicAction(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public scxmlxt_Expression getScxmlxt_expression() {
        return scxmlxt_expression;
    }

    public void setScxmlxt_expression(scxmlxt_Expression scxmlxt_expression) {
        this.scxmlxt_expression = scxmlxt_expression;
    }

}