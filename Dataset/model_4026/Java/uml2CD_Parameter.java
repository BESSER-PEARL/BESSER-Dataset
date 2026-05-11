





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Parameter  {

    private String defaultValue;
    private String kind;





    private uml2CD_DataType uml2cd_datatype;


    public uml2CD_Parameter(
        String defaultValue,        String kind    ) {
        this.defaultValue = defaultValue;
        this.kind = kind;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public uml2CD_DataType getUml2cd_datatype() {
        return uml2cd_datatype;
    }

    public void setUml2cd_datatype(uml2CD_DataType uml2cd_datatype) {
        this.uml2cd_datatype = uml2cd_datatype;
    }

}