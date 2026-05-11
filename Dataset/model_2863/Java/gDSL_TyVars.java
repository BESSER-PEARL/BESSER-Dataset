





import java.util.List;
import java.util.ArrayList;

public class gDSL_TyVars  {






    private gDSL_Type gdsl_type;




    private List<gDSL_Type> gdsl_types;




    private gDSL_DeclExport gdsl_declexport;


    public gDSL_TyVars(
    ) {
        this.gdsl_types = new ArrayList<>();
    }

    public gDSL_TyVars(
        ArrayList<gDSL_Type> gdsl_types    ) {
        this.gdsl_types = gdsl_types;
    }


    public gDSL_Type getGdsl_type() {
        return gdsl_type;
    }

    public void setGdsl_type(gDSL_Type gdsl_type) {
        this.gdsl_type = gdsl_type;
    }
    public List<gDSL_Type> getGdsl_types() {
        return gdsl_types;
    }

    public void addGdsl_type(Gdsl_type gdsl_type) {
        this.gdsl_types.add(gdsl_type);
    }
    public gDSL_DeclExport getGdsl_declexport() {
        return gdsl_declexport;
    }

    public void setGdsl_declexport(gDSL_DeclExport gdsl_declexport) {
        this.gdsl_declexport = gdsl_declexport;
    }

}