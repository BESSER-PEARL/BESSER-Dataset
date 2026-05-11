





import java.util.List;
import java.util.ArrayList;

public class idl_Preproc_Define extends Preproc {

    private String value;





    private idl_ConstExp idl_constexp;


    public idl_Preproc_Define(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public idl_ConstExp getIdl_constexp() {
        return idl_constexp;
    }

    public void setIdl_constexp(idl_ConstExp idl_constexp) {
        this.idl_constexp = idl_constexp;
    }

}