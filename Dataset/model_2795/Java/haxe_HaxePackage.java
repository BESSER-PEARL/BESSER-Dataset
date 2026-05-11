





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxePackage extends HaxePathReferentiable {






    private haxe_HaxePathReferentiable haxe_haxepathreferentiable;




    private List<haxe_HaxeType> haxe_haxetypes;




    private haxe_HaxePackage haxe_haxepackage;




    private List<haxe_HaxePathReferentiable> haxe_haxepathreferentiables;




    private haxe_HaxeModule haxe_haxemodule;


    public haxe_HaxePackage(
    ) {
        super(
        );
        this.haxe_haxetypes = new ArrayList<>();
        this.haxe_haxepathreferentiables = new ArrayList<>();
    }

    public haxe_HaxePackage(
        ArrayList<haxe_HaxeType> haxe_haxetypes,        ArrayList<haxe_HaxePathReferentiable> haxe_haxepathreferentiables    ) {
        this.haxe_haxetypes = haxe_haxetypes;
        this.haxe_haxepathreferentiables = haxe_haxepathreferentiables;
    }


    public haxe_HaxePathReferentiable getHaxe_haxepathreferentiable() {
        return haxe_haxepathreferentiable;
    }

    public void setHaxe_haxepathreferentiable(haxe_HaxePathReferentiable haxe_haxepathreferentiable) {
        this.haxe_haxepathreferentiable = haxe_haxepathreferentiable;
    }
    public List<haxe_HaxeType> getHaxe_haxetypes() {
        return haxe_haxetypes;
    }

    public void addHaxe_haxetype(Haxe_haxetype haxe_haxetype) {
        this.haxe_haxetypes.add(haxe_haxetype);
    }
    public haxe_HaxePackage getHaxe_haxepackage() {
        return haxe_haxepackage;
    }

    public void setHaxe_haxepackage(haxe_HaxePackage haxe_haxepackage) {
        this.haxe_haxepackage = haxe_haxepackage;
    }
    public List<haxe_HaxePathReferentiable> getHaxe_haxepathreferentiables() {
        return haxe_haxepathreferentiables;
    }

    public void addHaxe_haxepathreferentiable(Haxe_haxepathreferentiable haxe_haxepathreferentiable) {
        this.haxe_haxepathreferentiables.add(haxe_haxepathreferentiable);
    }
    public haxe_HaxeModule getHaxe_haxemodule() {
        return haxe_haxemodule;
    }

    public void setHaxe_haxemodule(haxe_HaxeModule haxe_haxemodule) {
        this.haxe_haxemodule = haxe_haxemodule;
    }

}