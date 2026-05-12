





import java.util.List;
import java.util.ArrayList;

public class XHTML_Label extends Attrs, Inlineforms {






    private ScriptExpression scriptexpression;




    private Character character;




    private List<Inline> inlines;




    private IDREF idref;




    private ScriptExpression scriptexpression;


    public XHTML_Label(
    ) {
        super(
        );
        this.inlines = new ArrayList<>();
    }

    public XHTML_Label(
        ArrayList<Inline> inlines    ) {
        this.inlines = inlines;
    }


    public ScriptExpression getScriptexpression() {
        return scriptexpression;
    }

    public void setScriptexpression(ScriptExpression scriptexpression) {
        this.scriptexpression = scriptexpression;
    }
    public Character getCharacter() {
        return character;
    }

    public void setCharacter(Character character) {
        this.character = character;
    }
    public List<Inline> getInlines() {
        return inlines;
    }

    public void addInline(Inline inline) {
        this.inlines.add(inline);
    }
    public IDREF getIdref() {
        return idref;
    }

    public void setIdref(IDREF idref) {
        this.idref = idref;
    }
    public ScriptExpression getScriptexpression() {
        return scriptexpression;
    }

    public void setScriptexpression(ScriptExpression scriptexpression) {
        this.scriptexpression = scriptexpression;
    }

}