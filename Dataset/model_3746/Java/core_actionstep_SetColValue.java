





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_SetColValue extends ActionStep {

    private String setAsDatatype;



    public core_actionstep_SetColValue(
        String setAsDatatype    ) {
        super(
        );
        this.setAsDatatype = setAsDatatype;
    }


    public String getSetasdatatype() {
        return setAsDatatype;
    }

    public void setSetasdatatype(String setAsDatatype) {
        this.setAsDatatype = setAsDatatype;
    }


}