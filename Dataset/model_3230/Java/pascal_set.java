





import java.util.List;
import java.util.ArrayList;

public class pascal_set  {

    private String brackets;





    private pascal_expression_list pascal_expression_list;


    public pascal_set(
        String brackets    ) {
        this.brackets = brackets;
    }


    public String getBrackets() {
        return brackets;
    }

    public void setBrackets(String brackets) {
        this.brackets = brackets;
    }

    public pascal_expression_list getPascal_expression_list() {
        return pascal_expression_list;
    }

    public void setPascal_expression_list(pascal_expression_list pascal_expression_list) {
        this.pascal_expression_list = pascal_expression_list;
    }

}