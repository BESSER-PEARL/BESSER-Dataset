





import java.util.List;
import java.util.ArrayList;

public class ast_DocumentationLine extends EJElement {

    private String text;





    private ast_EJBase ast_ejbase;


    public ast_DocumentationLine(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public ast_EJBase getAst_ejbase() {
        return ast_ejbase;
    }

    public void setAst_ejbase(ast_EJBase ast_ejbase) {
        this.ast_ejbase = ast_ejbase;
    }

}