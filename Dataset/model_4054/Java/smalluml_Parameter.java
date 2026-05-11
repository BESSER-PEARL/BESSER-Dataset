





import java.util.List;
import java.util.ArrayList;

public class smalluml_Parameter  {

    private String name;





    private smalluml_Operation smalluml_operation;




    private smalluml_Type smalluml_type;


    public smalluml_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smalluml_Operation getSmalluml_operation() {
        return smalluml_operation;
    }

    public void setSmalluml_operation(smalluml_Operation smalluml_operation) {
        this.smalluml_operation = smalluml_operation;
    }
    public smalluml_Type getSmalluml_type() {
        return smalluml_type;
    }

    public void setSmalluml_type(smalluml_Type smalluml_type) {
        this.smalluml_type = smalluml_type;
    }

}