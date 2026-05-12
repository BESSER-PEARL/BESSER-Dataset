





import java.util.List;
import java.util.ArrayList;

public class mmb_Modification  {

    private String VarName;
    private String VarType;





    private mmb_Mode mmb_mode;


    public mmb_Modification(
        String VarName,        String VarType    ) {
        this.VarName = VarName;
        this.VarType = VarType;
    }


    public String getVarname() {
        return VarName;
    }

    public void setVarname(String VarName) {
        this.VarName = VarName;
    }
    public String getVartype() {
        return VarType;
    }

    public void setVartype(String VarType) {
        this.VarType = VarType;
    }

    public mmb_Mode getMmb_mode() {
        return mmb_mode;
    }

    public void setMmb_mode(mmb_Mode mmb_mode) {
        this.mmb_mode = mmb_mode;
    }

}