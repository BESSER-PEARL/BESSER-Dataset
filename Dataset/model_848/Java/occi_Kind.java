





import java.util.List;
import java.util.ArrayList;

public class occi_Kind extends Type {






    private occi_Mixin occi_mixin;




    private List<occi_Kind> occi_kinds;




    private occi_Kind occi_kind;




    private List<occi_Kind> occi_kinds;


    public occi_Kind(
    ) {
        super(
        );
        this.occi_kinds = new ArrayList<>();
        this.occi_kinds = new ArrayList<>();
    }

    public occi_Kind(
        ArrayList<occi_Kind> occi_kinds,        ArrayList<occi_Kind> occi_kinds    ) {
        this.occi_kinds = occi_kinds;
        this.occi_kinds = occi_kinds;
    }


    public occi_Mixin getOcci_mixin() {
        return occi_mixin;
    }

    public void setOcci_mixin(occi_Mixin occi_mixin) {
        this.occi_mixin = occi_mixin;
    }
    public List<occi_Kind> getOcci_kinds() {
        return occi_kinds;
    }

    public void addOcci_kind(Occi_kind occi_kind) {
        this.occi_kinds.add(occi_kind);
    }
    public occi_Kind getOcci_kind() {
        return occi_kind;
    }

    public void setOcci_kind(occi_Kind occi_kind) {
        this.occi_kind = occi_kind;
    }
    public List<occi_Kind> getOcci_kinds() {
        return occi_kinds;
    }

    public void addOcci_kind(Occi_kind occi_kind) {
        this.occi_kinds.add(occi_kind);
    }

}