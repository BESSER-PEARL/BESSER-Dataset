





import java.util.List;
import java.util.ArrayList;

public class XHTML_Body extends Attrs {






    private List<Block> blocks;




    private ScriptExpression scriptexpression;




    private ScriptExpression scriptexpression;




    private Html html;


    public XHTML_Body(
    ) {
        super(
        );
        this.blocks = new ArrayList<>();
    }

    public XHTML_Body(
        ArrayList<Block> blocks    ) {
        this.blocks = blocks;
    }


    public List<Block> getBlocks() {
        return blocks;
    }

    public void addBlock(Block block) {
        this.blocks.add(block);
    }
    public ScriptExpression getScriptexpression() {
        return scriptexpression;
    }

    public void setScriptexpression(ScriptExpression scriptexpression) {
        this.scriptexpression = scriptexpression;
    }
    public ScriptExpression getScriptexpression() {
        return scriptexpression;
    }

    public void setScriptexpression(ScriptExpression scriptexpression) {
        this.scriptexpression = scriptexpression;
    }
    public Html getHtml() {
        return html;
    }

    public void setHtml(Html html) {
        this.html = html;
    }

}