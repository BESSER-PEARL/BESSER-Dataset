





import java.util.List;
import java.util.ArrayList;

public class uml_Parameter  {

    private String isStream;
    private String isException;
    private String default;





    private uml_ValueSpecification uml_valuespecification;


    public uml_Parameter(
        String isStream,        String isException,        String default    ) {
        this.isStream = isStream;
        this.isException = isException;
        this.default = default;
    }


    public String getIsstream() {
        return isStream;
    }

    public void setIsstream(String isStream) {
        this.isStream = isStream;
    }
    public String getIsexception() {
        return isException;
    }

    public void setIsexception(String isException) {
        this.isException = isException;
    }
    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public uml_ValueSpecification getUml_valuespecification() {
        return uml_valuespecification;
    }

    public void setUml_valuespecification(uml_ValueSpecification uml_valuespecification) {
        this.uml_valuespecification = uml_valuespecification;
    }

}