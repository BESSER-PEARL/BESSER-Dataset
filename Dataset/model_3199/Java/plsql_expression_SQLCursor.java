





import java.util.List;
import java.util.ArrayList;

public class plsql_expression_SQLCursor extends VarRefExpression {






    private CursorDeclaration cursordeclaration;


    public plsql_expression_SQLCursor(
    ) {
        super(
        );
    }



    public CursorDeclaration getCursordeclaration() {
        return cursordeclaration;
    }

    public void setCursordeclaration(CursorDeclaration cursordeclaration) {
        this.cursordeclaration = cursordeclaration;
    }

}