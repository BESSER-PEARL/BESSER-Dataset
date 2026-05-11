





import java.util.List;
import java.util.ArrayList;

public class idl_EventDcl extends Event {

    private boolean isCustom;
    private boolean isTruncatable;





    private List<idl_Export> idl_exports;




    private List<idl_ScopedName> idl_scopednames;




    private List<idl_ScopedName> idl_scopednames;


    public idl_EventDcl(
        boolean isCustom,        boolean isTruncatable    ) {
        super(
        );
        this.isCustom = isCustom;
        this.isTruncatable = isTruncatable;
        this.idl_exports = new ArrayList<>();
        this.idl_scopednames = new ArrayList<>();
        this.idl_scopednames = new ArrayList<>();
    }

    public idl_EventDcl(
        boolean isCustom,        boolean isTruncatable        ArrayList<idl_Export> idl_exports,        ArrayList<idl_ScopedName> idl_scopednames,        ArrayList<idl_ScopedName> idl_scopednames    ) {
        this.isCustom = isCustom;
        this.isTruncatable = isTruncatable;
        this.idl_exports = idl_exports;
        this.idl_scopednames = idl_scopednames;
        this.idl_scopednames = idl_scopednames;
    }

    public boolean getIscustom() {
        return isCustom;
    }

    public void setIscustom(boolean isCustom) {
        this.isCustom = isCustom;
    }
    public boolean getIstruncatable() {
        return isTruncatable;
    }

    public void setIstruncatable(boolean isTruncatable) {
        this.isTruncatable = isTruncatable;
    }

    public List<idl_Export> getIdl_exports() {
        return idl_exports;
    }

    public void addIdl_export(Idl_export idl_export) {
        this.idl_exports.add(idl_export);
    }
    public List<idl_ScopedName> getIdl_scopednames() {
        return idl_scopednames;
    }

    public void addIdl_scopedname(Idl_scopedname idl_scopedname) {
        this.idl_scopednames.add(idl_scopedname);
    }
    public List<idl_ScopedName> getIdl_scopednames() {
        return idl_scopednames;
    }

    public void addIdl_scopedname(Idl_scopedname idl_scopedname) {
        this.idl_scopednames.add(idl_scopedname);
    }

}