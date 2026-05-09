





import java.util.List;
import java.util.ArrayList;

public class mMDSL_OperatorAdd  {

    private String add;
    private String subtract;



    public mMDSL_OperatorAdd(
        String add,        String subtract    ) {
        this.add = add;
        this.subtract = subtract;
    }


    public String getAdd() {
        return add;
    }

    public void setAdd(String add) {
        this.add = add;
    }
    public String getSubtract() {
        return subtract;
    }

    public void setSubtract(String subtract) {
        this.subtract = subtract;
    }


}