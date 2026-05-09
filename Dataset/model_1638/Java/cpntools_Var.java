





import java.util.List;
import java.util.ArrayList;

public class cpntools_Var extends Declaration {

    private String idname;





    private cpntools_ColorSet cpntools_colorset;


    public cpntools_Var(
        String idname    ) {
        super(
        );
        this.idname = idname;
    }


    public String getIdname() {
        return idname;
    }

    public void setIdname(String idname) {
        this.idname = idname;
    }

    public cpntools_ColorSet getCpntools_colorset() {
        return cpntools_colorset;
    }

    public void setCpntools_colorset(cpntools_ColorSet cpntools_colorset) {
        this.cpntools_colorset = cpntools_colorset;
    }

}