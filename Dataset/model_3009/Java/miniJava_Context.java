





import java.util.List;
import java.util.ArrayList;

public class miniJava_Context  {






    private miniJava_Context minijava_context;




    private miniJava_Context minijava_context;




    private List<miniJava_SymbolToSymbolBindingMap> minijava_symboltosymbolbindingmaps;


    public miniJava_Context(
    ) {
        this.minijava_symboltosymbolbindingmaps = new ArrayList<>();
    }

    public miniJava_Context(
        ArrayList<miniJava_SymbolToSymbolBindingMap> minijava_symboltosymbolbindingmaps    ) {
        this.minijava_symboltosymbolbindingmaps = minijava_symboltosymbolbindingmaps;
    }


    public miniJava_Context getMinijava_context() {
        return minijava_context;
    }

    public void setMinijava_context(miniJava_Context minijava_context) {
        this.minijava_context = minijava_context;
    }
    public miniJava_Context getMinijava_context() {
        return minijava_context;
    }

    public void setMinijava_context(miniJava_Context minijava_context) {
        this.minijava_context = minijava_context;
    }
    public List<miniJava_SymbolToSymbolBindingMap> getMinijava_symboltosymbolbindingmaps() {
        return minijava_symboltosymbolbindingmaps;
    }

    public void addMinijava_symboltosymbolbindingmap(Minijava_symboltosymbolbindingmap minijava_symboltosymbolbindingmap) {
        this.minijava_symboltosymbolbindingmaps.add(minijava_symboltosymbolbindingmap);
    }

}