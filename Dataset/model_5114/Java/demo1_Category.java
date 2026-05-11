





import java.util.List;
import java.util.ArrayList;

public class demo1_Category  {

    private String name;





    private demo1_TestExpression demo1_testexpression;




    private demo1_Model demo1_model;


    public demo1_Category(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public demo1_TestExpression getDemo1_testexpression() {
        return demo1_testexpression;
    }

    public void setDemo1_testexpression(demo1_TestExpression demo1_testexpression) {
        this.demo1_testexpression = demo1_testexpression;
    }
    public demo1_Model getDemo1_model() {
        return demo1_model;
    }

    public void setDemo1_model(demo1_Model demo1_model) {
        this.demo1_model = demo1_model;
    }

}