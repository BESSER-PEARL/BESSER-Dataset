





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeHaxedocComment extends HaxeComment {






    private List<haxe_HaxeTagElement> haxe_haxetagelements;


    public haxe_HaxeHaxedocComment(
    ) {
        super(
        );
        this.haxe_haxetagelements = new ArrayList<>();
    }

    public haxe_HaxeHaxedocComment(
        ArrayList<haxe_HaxeTagElement> haxe_haxetagelements    ) {
        this.haxe_haxetagelements = haxe_haxetagelements;
    }


    public List<haxe_HaxeTagElement> getHaxe_haxetagelements() {
        return haxe_haxetagelements;
    }

    public void addHaxe_haxetagelement(Haxe_haxetagelement haxe_haxetagelement) {
        this.haxe_haxetagelements.add(haxe_haxetagelement);
    }

}