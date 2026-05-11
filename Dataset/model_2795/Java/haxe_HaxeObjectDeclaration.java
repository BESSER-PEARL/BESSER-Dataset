





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeObjectDeclaration extends HaxeExpression {






    private List<haxe_HaxeFieldDeclaration> haxe_haxefielddeclarations;




    private haxe_HaxeTypeAccess haxe_haxetypeaccess;


    public haxe_HaxeObjectDeclaration(
    ) {
        super(
        );
        this.haxe_haxefielddeclarations = new ArrayList<>();
    }

    public haxe_HaxeObjectDeclaration(
        ArrayList<haxe_HaxeFieldDeclaration> haxe_haxefielddeclarations    ) {
        this.haxe_haxefielddeclarations = haxe_haxefielddeclarations;
    }


    public List<haxe_HaxeFieldDeclaration> getHaxe_haxefielddeclarations() {
        return haxe_haxefielddeclarations;
    }

    public void addHaxe_haxefielddeclaration(Haxe_haxefielddeclaration haxe_haxefielddeclaration) {
        this.haxe_haxefielddeclarations.add(haxe_haxefielddeclaration);
    }
    public haxe_HaxeTypeAccess getHaxe_haxetypeaccess() {
        return haxe_haxetypeaccess;
    }

    public void setHaxe_haxetypeaccess(haxe_HaxeTypeAccess haxe_haxetypeaccess) {
        this.haxe_haxetypeaccess = haxe_haxetypeaccess;
    }

}