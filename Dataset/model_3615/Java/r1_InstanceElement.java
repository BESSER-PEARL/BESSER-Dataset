





import java.util.List;
import java.util.ArrayList;

public class r1_InstanceElement  {

    private String name;





    private r1_Expression r1_expression;




    private r1_Instance r1_instance;


    public r1_InstanceElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public r1_Expression getR1_expression() {
        return r1_expression;
    }

    public void setR1_expression(r1_Expression r1_expression) {
        this.r1_expression = r1_expression;
    }
    public r1_Instance getR1_instance() {
        return r1_instance;
    }

    public void setR1_instance(r1_Instance r1_instance) {
        this.r1_instance = r1_instance;
    }

}