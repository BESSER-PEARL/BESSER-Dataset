





import java.util.List;
import java.util.ArrayList;

public class robo_expression_Variable extends Expr {

    private String name;



    public robo_expression_Variable(
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