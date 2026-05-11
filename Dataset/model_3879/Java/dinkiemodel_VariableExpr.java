





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_VariableExpr extends Expression {

    private String name;



    public dinkiemodel_VariableExpr(
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