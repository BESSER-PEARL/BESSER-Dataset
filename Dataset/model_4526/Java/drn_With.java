





import java.util.List;
import java.util.ArrayList;

public class drn_With  {

    private String name;





    private drn_Expression drn_expression;


    public drn_With(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public drn_Expression getDrn_expression() {
        return drn_expression;
    }

    public void setDrn_expression(drn_Expression drn_expression) {
        this.drn_expression = drn_expression;
    }

}