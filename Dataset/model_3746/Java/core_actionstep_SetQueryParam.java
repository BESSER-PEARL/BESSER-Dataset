





import java.util.List;
import java.util.ArrayList;

public class core_actionstep_SetQueryParam extends ActionStep {

    private String paramDatatype;



    public core_actionstep_SetQueryParam(
        String paramDatatype    ) {
        super(
        );
        this.paramDatatype = paramDatatype;
    }


    public String getParamdatatype() {
        return paramDatatype;
    }

    public void setParamdatatype(String paramDatatype) {
        this.paramDatatype = paramDatatype;
    }


}