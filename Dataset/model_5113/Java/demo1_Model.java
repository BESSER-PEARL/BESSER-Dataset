





import java.util.List;
import java.util.ArrayList;

public class demo1_Model  {






    private List<demo1_Category> demo1_categorys;




    private demo1_Rule demo1_rule;


    public demo1_Model(
    ) {
        this.demo1_categorys = new ArrayList<>();
    }

    public demo1_Model(
        ArrayList<demo1_Category> demo1_categorys    ) {
        this.demo1_categorys = demo1_categorys;
    }


    public List<demo1_Category> getDemo1_categorys() {
        return demo1_categorys;
    }

    public void addDemo1_category(Demo1_category demo1_category) {
        this.demo1_categorys.add(demo1_category);
    }
    public demo1_Rule getDemo1_rule() {
        return demo1_rule;
    }

    public void setDemo1_rule(demo1_Rule demo1_rule) {
        this.demo1_rule = demo1_rule;
    }

}