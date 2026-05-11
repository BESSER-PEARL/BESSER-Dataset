





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeFunctionTypeAccess extends HaxeTypeAccess {






    private List<haxe_HaxeTypeAccess> haxe_haxetypeaccesss;




    private haxe_HaxeTypeAccess haxe_haxetypeaccess;


    public haxe_HaxeFunctionTypeAccess(
    ) {
        super(
        );
        this.haxe_haxetypeaccesss = new ArrayList<>();
    }

    public haxe_HaxeFunctionTypeAccess(
        ArrayList<haxe_HaxeTypeAccess> haxe_haxetypeaccesss    ) {
        this.haxe_haxetypeaccesss = haxe_haxetypeaccesss;
    }


    public List<haxe_HaxeTypeAccess> getHaxe_haxetypeaccesss() {
        return haxe_haxetypeaccesss;
    }

    public void addHaxe_haxetypeaccess(Haxe_haxetypeaccess haxe_haxetypeaccess) {
        this.haxe_haxetypeaccesss.add(haxe_haxetypeaccess);
    }
    public haxe_HaxeTypeAccess getHaxe_haxetypeaccess() {
        return haxe_haxetypeaccess;
    }

    public void setHaxe_haxetypeaccess(haxe_HaxeTypeAccess haxe_haxetypeaccess) {
        this.haxe_haxetypeaccess = haxe_haxetypeaccess;
    }

}