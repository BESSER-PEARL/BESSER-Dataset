





import java.util.List;
import java.util.ArrayList;

public class Docbook_ParameterType  {

    private String mixed;





    private Docbook_ParamdefType docbook_paramdeftype;


    public Docbook_ParameterType(
        String mixed    ) {
        this.mixed = mixed;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_ParamdefType getDocbook_paramdeftype() {
        return docbook_paramdeftype;
    }

    public void setDocbook_paramdeftype(Docbook_ParamdefType docbook_paramdeftype) {
        this.docbook_paramdeftype = docbook_paramdeftype;
    }

}