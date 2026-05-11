





import java.util.List;
import java.util.ArrayList;

public class idl_CaseLabel  {

    private boolean isDefault;
    private boolean isCase;





    private idl_Case idl_case;




    private idl_ConstExp idl_constexp;


    public idl_CaseLabel(
        boolean isDefault,        boolean isCase    ) {
        this.isDefault = isDefault;
        this.isCase = isCase;
    }


    public boolean getIsdefault() {
        return isDefault;
    }

    public void setIsdefault(boolean isDefault) {
        this.isDefault = isDefault;
    }
    public boolean getIscase() {
        return isCase;
    }

    public void setIscase(boolean isCase) {
        this.isCase = isCase;
    }

    public idl_Case getIdl_case() {
        return idl_case;
    }

    public void setIdl_case(idl_Case idl_case) {
        this.idl_case = idl_case;
    }
    public idl_ConstExp getIdl_constexp() {
        return idl_constexp;
    }

    public void setIdl_constexp(idl_ConstExp idl_constexp) {
        this.idl_constexp = idl_constexp;
    }

}