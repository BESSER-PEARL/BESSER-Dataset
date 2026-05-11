





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeClassifierAccess extends HaxePathReference, HaxeTypeAccess {






    private haxe_HaxeClass haxe_haxeclass;




    private haxe_HaxeClass haxe_haxeclass;




    private List<haxe_HaxeTypeAccess> haxe_haxetypeaccesss;


    public haxe_HaxeClassifierAccess(
    ) {
        super(
        );
        this.haxe_haxetypeaccesss = new ArrayList<>();
    }

    public haxe_HaxeClassifierAccess(
        ArrayList<haxe_HaxeTypeAccess> haxe_haxetypeaccesss    ) {
        this.haxe_haxetypeaccesss = haxe_haxetypeaccesss;
    }


    public haxe_HaxeClass getHaxe_haxeclass() {
        return haxe_haxeclass;
    }

    public void setHaxe_haxeclass(haxe_HaxeClass haxe_haxeclass) {
        this.haxe_haxeclass = haxe_haxeclass;
    }
    public haxe_HaxeClass getHaxe_haxeclass() {
        return haxe_haxeclass;
    }

    public void setHaxe_haxeclass(haxe_HaxeClass haxe_haxeclass) {
        this.haxe_haxeclass = haxe_haxeclass;
    }
    public List<haxe_HaxeTypeAccess> getHaxe_haxetypeaccesss() {
        return haxe_haxetypeaccesss;
    }

    public void addHaxe_haxetypeaccess(Haxe_haxetypeaccess haxe_haxetypeaccess) {
        this.haxe_haxetypeaccesss.add(haxe_haxetypeaccess);
    }

}