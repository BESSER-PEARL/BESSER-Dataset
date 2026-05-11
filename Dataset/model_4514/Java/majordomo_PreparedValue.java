





import java.util.List;
import java.util.ArrayList;

public class majordomo_PreparedValue  {

    private String name;





    private majordomo_ValueExpression majordomo_valueexpression;




    private majordomo_ValueReference majordomo_valuereference;


    public majordomo_PreparedValue(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public majordomo_ValueExpression getMajordomo_valueexpression() {
        return majordomo_valueexpression;
    }

    public void setMajordomo_valueexpression(majordomo_ValueExpression majordomo_valueexpression) {
        this.majordomo_valueexpression = majordomo_valueexpression;
    }
    public majordomo_ValueReference getMajordomo_valuereference() {
        return majordomo_valuereference;
    }

    public void setMajordomo_valuereference(majordomo_ValueReference majordomo_valuereference) {
        this.majordomo_valuereference = majordomo_valuereference;
    }

}