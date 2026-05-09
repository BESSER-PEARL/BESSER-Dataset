





import java.util.List;
import java.util.ArrayList;

public class ocl_exp_EVariable  {

    private String name;





    private EOclExpression eoclexpression;


    public ocl_exp_EVariable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public EOclExpression getEoclexpression() {
        return eoclexpression;
    }

    public void setEoclexpression(EOclExpression eoclexpression) {
        this.eoclexpression = eoclexpression;
    }

}