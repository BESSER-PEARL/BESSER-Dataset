





import java.util.List;
import java.util.ArrayList;

public class myDsl_IDENTIFIER extends direct_declarator, identifier_list, struct_or_union_specifier, postfix_expressionR, designator, labeled_statement, identifier_listR, jump_statement, primary_expression {

    private String name;



    public myDsl_IDENTIFIER(
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


}