





import java.util.List;
import java.util.ArrayList;

public class fiacre_State  {

    private String name;





    private fiacre_ProcessDecl fiacre_processdecl;


    public fiacre_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fiacre_ProcessDecl getFiacre_processdecl() {
        return fiacre_processdecl;
    }

    public void setFiacre_processdecl(fiacre_ProcessDecl fiacre_processdecl) {
        this.fiacre_processdecl = fiacre_processdecl;
    }

}