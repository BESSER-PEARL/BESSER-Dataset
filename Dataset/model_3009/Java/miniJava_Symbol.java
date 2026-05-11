





import java.util.List;
import java.util.ArrayList;

public class miniJava_Symbol extends TypedDeclaration {






    private miniJava_SymbolToSymbolBindingMap minijava_symboltosymbolbindingmap;




    private miniJava_SymbolBinding minijava_symbolbinding;




    private miniJava_SymbolRef minijava_symbolref;


    public miniJava_Symbol(
    ) {
        super(
        );
    }



    public miniJava_SymbolToSymbolBindingMap getMinijava_symboltosymbolbindingmap() {
        return minijava_symboltosymbolbindingmap;
    }

    public void setMinijava_symboltosymbolbindingmap(miniJava_SymbolToSymbolBindingMap minijava_symboltosymbolbindingmap) {
        this.minijava_symboltosymbolbindingmap = minijava_symboltosymbolbindingmap;
    }
    public miniJava_SymbolBinding getMinijava_symbolbinding() {
        return minijava_symbolbinding;
    }

    public void setMinijava_symbolbinding(miniJava_SymbolBinding minijava_symbolbinding) {
        this.minijava_symbolbinding = minijava_symbolbinding;
    }
    public miniJava_SymbolRef getMinijava_symbolref() {
        return minijava_symbolref;
    }

    public void setMinijava_symbolref(miniJava_SymbolRef minijava_symbolref) {
        this.minijava_symbolref = minijava_symbolref;
    }

}