





import java.util.List;
import java.util.ArrayList;

public class sADL_OrderElement  {

    private boolean desc;





    private sADL_SadlResource sadl_sadlresource;




    private sADL_SelectExpression sadl_selectexpression;


    public sADL_OrderElement(
        boolean desc    ) {
        this.desc = desc;
    }


    public boolean getDesc() {
        return desc;
    }

    public void setDesc(boolean desc) {
        this.desc = desc;
    }

    public sADL_SadlResource getSadl_sadlresource() {
        return sadl_sadlresource;
    }

    public void setSadl_sadlresource(sADL_SadlResource sadl_sadlresource) {
        this.sadl_sadlresource = sadl_sadlresource;
    }
    public sADL_SelectExpression getSadl_selectexpression() {
        return sadl_selectexpression;
    }

    public void setSadl_selectexpression(sADL_SelectExpression sadl_selectexpression) {
        this.sadl_selectexpression = sadl_selectexpression;
    }

}