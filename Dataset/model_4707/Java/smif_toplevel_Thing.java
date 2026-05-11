





import java.util.List;
import java.util.ArrayList;

public class smif_toplevel_Thing  {






    private LexicalScope lexicalscope;




    private List<Context> contexts;




    private LexicalScope lexicalscope;




    private List<Type> types;




    private List<PropertyBinding> propertybindings;


    public smif_toplevel_Thing(
    ) {
        this.contexts = new ArrayList<>();
        this.types = new ArrayList<>();
        this.propertybindings = new ArrayList<>();
    }

    public smif_toplevel_Thing(
        ArrayList<Context> contexts,        ArrayList<Type> types,        ArrayList<PropertyBinding> propertybindings    ) {
        this.contexts = contexts;
        this.types = types;
        this.propertybindings = propertybindings;
    }


    public LexicalScope getLexicalscope() {
        return lexicalscope;
    }

    public void setLexicalscope(LexicalScope lexicalscope) {
        this.lexicalscope = lexicalscope;
    }
    public List<Context> getContexts() {
        return contexts;
    }

    public void addContext(Context context) {
        this.contexts.add(context);
    }
    public LexicalScope getLexicalscope() {
        return lexicalscope;
    }

    public void setLexicalscope(LexicalScope lexicalscope) {
        this.lexicalscope = lexicalscope;
    }
    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public List<PropertyBinding> getPropertybindings() {
        return propertybindings;
    }

    public void addPropertybinding(Propertybinding propertybinding) {
        this.propertybindings.add(propertybinding);
    }

}