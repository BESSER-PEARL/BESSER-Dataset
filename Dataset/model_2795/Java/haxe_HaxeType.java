





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeType extends HaxePathReferentiable, HaxeASTNode {

    private boolean private;
    private boolean extern;





    private List<haxe_HaxeComment> haxe_haxecomments;




    private haxe_HaxeModule haxe_haxemodule;




    private haxe_HaxeModule haxe_haxemodule;




    private List<haxe_HaxeComment> haxe_haxecomments;


    public haxe_HaxeType(
        boolean private,        boolean extern    ) {
        super(
        );
        this.private = private;
        this.extern = extern;
        this.haxe_haxecomments = new ArrayList<>();
        this.haxe_haxecomments = new ArrayList<>();
    }

    public haxe_HaxeType(
        boolean private,        boolean extern        ArrayList<haxe_HaxeComment> haxe_haxecomments,        ArrayList<haxe_HaxeComment> haxe_haxecomments    ) {
        this.private = private;
        this.extern = extern;
        this.haxe_haxecomments = haxe_haxecomments;
        this.haxe_haxecomments = haxe_haxecomments;
    }

    public boolean getPrivate() {
        return private;
    }

    public void setPrivate(boolean private) {
        this.private = private;
    }
    public boolean getExtern() {
        return extern;
    }

    public void setExtern(boolean extern) {
        this.extern = extern;
    }

    public List<haxe_HaxeComment> getHaxe_haxecomments() {
        return haxe_haxecomments;
    }

    public void addHaxe_haxecomment(Haxe_haxecomment haxe_haxecomment) {
        this.haxe_haxecomments.add(haxe_haxecomment);
    }
    public haxe_HaxeModule getHaxe_haxemodule() {
        return haxe_haxemodule;
    }

    public void setHaxe_haxemodule(haxe_HaxeModule haxe_haxemodule) {
        this.haxe_haxemodule = haxe_haxemodule;
    }
    public haxe_HaxeModule getHaxe_haxemodule() {
        return haxe_haxemodule;
    }

    public void setHaxe_haxemodule(haxe_HaxeModule haxe_haxemodule) {
        this.haxe_haxemodule = haxe_haxemodule;
    }
    public List<haxe_HaxeComment> getHaxe_haxecomments() {
        return haxe_haxecomments;
    }

    public void addHaxe_haxecomment(Haxe_haxecomment haxe_haxecomment) {
        this.haxe_haxecomments.add(haxe_haxecomment);
    }

}