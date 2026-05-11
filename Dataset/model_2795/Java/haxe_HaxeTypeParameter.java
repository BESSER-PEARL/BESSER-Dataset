





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeTypeParameter extends HaxeType {






    private List<haxe_HaxeTypeAccess> haxe_haxetypeaccesss;




    private haxe_HaxeType haxe_haxetype;




    private haxe_HaxeAbstractFunction haxe_haxeabstractfunction;


    public haxe_HaxeTypeParameter(
    ) {
        super(
        );
        this.haxe_haxetypeaccesss = new ArrayList<>();
    }

    public haxe_HaxeTypeParameter(
        ArrayList<haxe_HaxeTypeAccess> haxe_haxetypeaccesss    ) {
        this.haxe_haxetypeaccesss = haxe_haxetypeaccesss;
    }


    public List<haxe_HaxeTypeAccess> getHaxe_haxetypeaccesss() {
        return haxe_haxetypeaccesss;
    }

    public void addHaxe_haxetypeaccess(Haxe_haxetypeaccess haxe_haxetypeaccess) {
        this.haxe_haxetypeaccesss.add(haxe_haxetypeaccess);
    }
    public haxe_HaxeType getHaxe_haxetype() {
        return haxe_haxetype;
    }

    public void setHaxe_haxetype(haxe_HaxeType haxe_haxetype) {
        this.haxe_haxetype = haxe_haxetype;
    }
    public haxe_HaxeAbstractFunction getHaxe_haxeabstractfunction() {
        return haxe_haxeabstractfunction;
    }

    public void setHaxe_haxeabstractfunction(haxe_HaxeAbstractFunction haxe_haxeabstractfunction) {
        this.haxe_haxeabstractfunction = haxe_haxeabstractfunction;
    }

}