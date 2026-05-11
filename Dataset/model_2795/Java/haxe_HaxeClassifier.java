





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeClassifier extends HaxeMetadataContainer, HaxeType, HaxeFieldContainer {






    private List<haxe_HaxeOperation> haxe_haxeoperations;




    private haxe_HaxePackage haxe_haxepackage;


    public haxe_HaxeClassifier(
    ) {
        super(
        );
        this.haxe_haxeoperations = new ArrayList<>();
    }

    public haxe_HaxeClassifier(
        ArrayList<haxe_HaxeOperation> haxe_haxeoperations    ) {
        this.haxe_haxeoperations = haxe_haxeoperations;
    }


    public List<haxe_HaxeOperation> getHaxe_haxeoperations() {
        return haxe_haxeoperations;
    }

    public void addHaxe_haxeoperation(Haxe_haxeoperation haxe_haxeoperation) {
        this.haxe_haxeoperations.add(haxe_haxeoperation);
    }
    public haxe_HaxePackage getHaxe_haxepackage() {
        return haxe_haxepackage;
    }

    public void setHaxe_haxepackage(haxe_HaxePackage haxe_haxepackage) {
        this.haxe_haxepackage = haxe_haxepackage;
    }

}