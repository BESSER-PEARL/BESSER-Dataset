





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeEnumConstructor extends HaxeVariableDeclaration, HaxeField {






    private List<haxe_HaxeSingleVariableDeclaration> haxe_haxesinglevariabledeclarations;


    public haxe_HaxeEnumConstructor(
    ) {
        super(
        );
        this.haxe_haxesinglevariabledeclarations = new ArrayList<>();
    }

    public haxe_HaxeEnumConstructor(
        ArrayList<haxe_HaxeSingleVariableDeclaration> haxe_haxesinglevariabledeclarations    ) {
        this.haxe_haxesinglevariabledeclarations = haxe_haxesinglevariabledeclarations;
    }


    public List<haxe_HaxeSingleVariableDeclaration> getHaxe_haxesinglevariabledeclarations() {
        return haxe_haxesinglevariabledeclarations;
    }

    public void addHaxe_haxesinglevariabledeclaration(Haxe_haxesinglevariabledeclaration haxe_haxesinglevariabledeclaration) {
        this.haxe_haxesinglevariabledeclarations.add(haxe_haxesinglevariabledeclaration);
    }

}