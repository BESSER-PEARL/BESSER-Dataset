





import java.util.List;
import java.util.ArrayList;

public class esper_SelectAttributesDefinition  {

    private String operator;





    private esper_Select esper_select;


    public esper_SelectAttributesDefinition(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public esper_Select getEsper_select() {
        return esper_select;
    }

    public void setEsper_select(esper_Select esper_select) {
        this.esper_select = esper_select;
    }

}