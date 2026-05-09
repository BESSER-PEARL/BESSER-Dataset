





import java.util.List;
import java.util.ArrayList;

public class eol_AnyType extends Type {

    private boolean declared;





    private List<eol_Type> eol_types;


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

}