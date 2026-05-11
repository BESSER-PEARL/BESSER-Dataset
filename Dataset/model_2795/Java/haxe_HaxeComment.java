





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeComment extends HaxeASTNode {

    private boolean prefixOfParent;
    private boolean lineComment;
    private String content;
    private boolean enclosedByParent;





    private haxe_HaxeASTNode haxe_haxeastnode;




    private haxe_HaxeModule haxe_haxemodule;


    public haxe_HaxeComment(
        boolean prefixOfParent,        boolean lineComment,        String content,        boolean enclosedByParent    ) {
        super(
        );
        this.prefixOfParent = prefixOfParent;
        this.lineComment = lineComment;
        this.content = content;
        this.enclosedByParent = enclosedByParent;
    }


    public boolean getPrefixofparent() {
        return prefixOfParent;
    }

    public void setPrefixofparent(boolean prefixOfParent) {
        this.prefixOfParent = prefixOfParent;
    }
    public boolean getLinecomment() {
        return lineComment;
    }

    public void setLinecomment(boolean lineComment) {
        this.lineComment = lineComment;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public boolean getEnclosedbyparent() {
        return enclosedByParent;
    }

    public void setEnclosedbyparent(boolean enclosedByParent) {
        this.enclosedByParent = enclosedByParent;
    }

    public haxe_HaxeASTNode getHaxe_haxeastnode() {
        return haxe_haxeastnode;
    }

    public void setHaxe_haxeastnode(haxe_HaxeASTNode haxe_haxeastnode) {
        this.haxe_haxeastnode = haxe_haxeastnode;
    }
    public haxe_HaxeModule getHaxe_haxemodule() {
        return haxe_haxemodule;
    }

    public void setHaxe_haxemodule(haxe_HaxeModule haxe_haxemodule) {
        this.haxe_haxemodule = haxe_haxemodule;
    }

}