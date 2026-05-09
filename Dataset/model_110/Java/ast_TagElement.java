





import java.util.List;
import java.util.ArrayList;

public class ast_TagElement extends ASTNode, IDocElement {

    private String tagName;





    private List<ast_IDocElement> ast_idocelements;


    public ast_TagElement(
        String tagName    ) {
        super(
        );
        this.tagName = tagName;
        this.ast_idocelements = new ArrayList<>();
    }

    public ast_TagElement(
        String tagName        ArrayList<ast_IDocElement> ast_idocelements    ) {
        this.tagName = tagName;
        this.ast_idocelements = ast_idocelements;
    }

    public String getTagname() {
        return tagName;
    }

    public void setTagname(String tagName) {
        this.tagName = tagName;
    }

    public List<ast_IDocElement> getAst_idocelements() {
        return ast_idocelements;
    }

    public void addAst_idocelement(Ast_idocelement ast_idocelement) {
        this.ast_idocelements.add(ast_idocelement);
    }

}