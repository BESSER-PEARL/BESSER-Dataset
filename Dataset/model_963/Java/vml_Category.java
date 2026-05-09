





import java.util.List;
import java.util.ArrayList;

public class vml_Category  {

    private String category;





    private vml_StackBarChart vml_stackbarchart;




    private vml_StackBars vml_stackbars;


    public vml_Category(
        String category    ) {
        this.category = category;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public vml_StackBarChart getVml_stackbarchart() {
        return vml_stackbarchart;
    }

    public void setVml_stackbarchart(vml_StackBarChart vml_stackbarchart) {
        this.vml_stackbarchart = vml_stackbarchart;
    }
    public vml_StackBars getVml_stackbars() {
        return vml_stackbars;
    }

    public void setVml_stackbars(vml_StackBars vml_stackbars) {
        this.vml_stackbars = vml_stackbars;
    }

}