





import java.util.List;
import java.util.ArrayList;

public class eol_types_AnyType extends Type {

    private boolean declared;





    private List<eol_types_Type> eol_types_types;


    public eol_types_AnyType(
        boolean declared    ) {
        super(
        );
        this.declared = declared;
        this.eol_types_types = new ArrayList<>();
    }

    public eol_types_AnyType(
        boolean declared        ArrayList<eol_types_Type> eol_types_types    ) {
        this.declared = declared;
        this.eol_types_types = eol_types_types;
    }

    public boolean getDeclared() {
        return declared;
    }

    public void setDeclared(boolean declared) {
        this.declared = declared;
    }

    public List<eol_types_Type> getEol_types_types() {
        return eol_types_types;
    }

    public void addEol_types_type(Eol_types_type eol_types_type) {
        this.eol_types_types.add(eol_types_type);
    }

}