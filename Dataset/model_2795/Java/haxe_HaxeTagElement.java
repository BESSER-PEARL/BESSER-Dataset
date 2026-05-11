





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeTagElement extends HaxeASTNode {

    private String tagName;





    private List<haxe_HaxeASTNode> haxe_haxeastnodes;


    public haxe_HaxeTagElement(
        String tagName    ) {
        super(
        );
        this.tagName = tagName;
        this.haxe_haxeastnodes = new ArrayList<>();
    }

    public haxe_HaxeTagElement(
        String tagName        ArrayList<haxe_HaxeASTNode> haxe_haxeastnodes    ) {
        this.tagName = tagName;
        this.haxe_haxeastnodes = haxe_haxeastnodes;
    }

    public String getTagname() {
        return tagName;
    }

    public void setTagname(String tagName) {
        this.tagName = tagName;
    }

    public List<haxe_HaxeASTNode> getHaxe_haxeastnodes() {
        return haxe_haxeastnodes;
    }

    public void addHaxe_haxeastnode(Haxe_haxeastnode haxe_haxeastnode) {
        this.haxe_haxeastnodes.add(haxe_haxeastnode);
    }

}