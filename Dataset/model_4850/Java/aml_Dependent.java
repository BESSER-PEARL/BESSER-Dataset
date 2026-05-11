





import java.util.List;
import java.util.ArrayList;

public class aml_Dependent  {

    private String idRef;
    private String ordinal;



    public aml_Dependent(
        String idRef,        String ordinal    ) {
        this.idRef = idRef;
        this.ordinal = ordinal;
    }


    public String getIdref() {
        return idRef;
    }

    public void setIdref(String idRef) {
        this.idRef = idRef;
    }
    public String getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(String ordinal) {
        this.ordinal = ordinal;
    }


}