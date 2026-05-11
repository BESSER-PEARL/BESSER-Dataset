





import java.util.List;
import java.util.ArrayList;

public class cgimodel_Expr  {

    private String value;





    private cgimodel_State cgimodel_state;


    public cgimodel_Expr(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public cgimodel_State getCgimodel_state() {
        return cgimodel_state;
    }

    public void setCgimodel_state(cgimodel_State cgimodel_state) {
        this.cgimodel_state = cgimodel_state;
    }

}