





import java.util.List;
import java.util.ArrayList;

public class scxmlxt_VarRef extends Expression {






    private scxmlxt_EPath scxmlxt_epath;




    private scxmlxt_VarDef scxmlxt_vardef;


    public scxmlxt_VarRef(
    ) {
        super(
        );
    }



    public scxmlxt_EPath getScxmlxt_epath() {
        return scxmlxt_epath;
    }

    public void setScxmlxt_epath(scxmlxt_EPath scxmlxt_epath) {
        this.scxmlxt_epath = scxmlxt_epath;
    }
    public scxmlxt_VarDef getScxmlxt_vardef() {
        return scxmlxt_vardef;
    }

    public void setScxmlxt_vardef(scxmlxt_VarDef scxmlxt_vardef) {
        this.scxmlxt_vardef = scxmlxt_vardef;
    }

}