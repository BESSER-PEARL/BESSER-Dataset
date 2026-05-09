





import java.util.List;
import java.util.ArrayList;

public class simpleocl_OclModelElementExp extends OclExpression {

    private String name;



    public simpleocl_OclModelElementExp(
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