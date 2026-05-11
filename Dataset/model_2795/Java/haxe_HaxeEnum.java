





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeEnum extends HaxeClassifier {






    private List<haxe_HaxeEnumConstructor> haxe_haxeenumconstructors;


    public haxe_HaxeEnum(
    ) {
        super(
        );
        this.haxe_haxeenumconstructors = new ArrayList<>();
    }

    public haxe_HaxeEnum(
        ArrayList<haxe_HaxeEnumConstructor> haxe_haxeenumconstructors    ) {
        this.haxe_haxeenumconstructors = haxe_haxeenumconstructors;
    }


    public List<haxe_HaxeEnumConstructor> getHaxe_haxeenumconstructors() {
        return haxe_haxeenumconstructors;
    }

    public void addHaxe_haxeenumconstructor(Haxe_haxeenumconstructor haxe_haxeenumconstructor) {
        this.haxe_haxeenumconstructors.add(haxe_haxeenumconstructor);
    }

}