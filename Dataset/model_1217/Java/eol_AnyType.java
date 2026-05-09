





import java.util.List;
import java.util.ArrayList;

public class eol_AnyType extends Type {

    private boolean declared;





    private List<eol_Type> eol_types;




    private eol_MapType eol_maptype;




    private eol_MapType eol_maptype;


    public eol_AnyType(
        boolean declared    ) {
        super(
        );
        this.declared = declared;
        this.eol_types = new ArrayList<>();
    }

    public eol_AnyType(
        boolean declared        ArrayList<eol_Type> eol_types    ) {
        this.declared = declared;
        this.eol_types = eol_types;
    }

    public boolean getDeclared() {
        return declared;
    }

    public void setDeclared(boolean declared) {
        this.declared = declared;
    }

    public List<eol_Type> getEol_types() {
        return eol_types;
    }

    public void addEol_type(Eol_type eol_type) {
        this.eol_types.add(eol_type);
    }
    public eol_MapType getEol_maptype() {
        return eol_maptype;
    }

    public void setEol_maptype(eol_MapType eol_maptype) {
        this.eol_maptype = eol_maptype;
    }
    public eol_MapType getEol_maptype() {
        return eol_maptype;
    }

    public void setEol_maptype(eol_MapType eol_maptype) {
        this.eol_maptype = eol_maptype;
    }

}