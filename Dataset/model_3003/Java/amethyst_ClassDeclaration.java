





import java.util.List;
import java.util.ArrayList;

public class amethyst_ClassDeclaration extends Symbol {






    private List<amethyst_Symbol> amethyst_symbols;




    private amethyst_ClassDeclaration amethyst_classdeclaration;




    private List<amethyst_Symbol> amethyst_symbols;




    private amethyst_ClassType amethyst_classtype;




    private amethyst_TagDeclaration amethyst_tagdeclaration;


    public amethyst_ClassDeclaration(
    ) {
        super(
        );
        this.amethyst_symbols = new ArrayList<>();
        this.amethyst_symbols = new ArrayList<>();
    }

    public amethyst_ClassDeclaration(
        ArrayList<amethyst_Symbol> amethyst_symbols,        ArrayList<amethyst_Symbol> amethyst_symbols    ) {
        this.amethyst_symbols = amethyst_symbols;
        this.amethyst_symbols = amethyst_symbols;
    }


    public List<amethyst_Symbol> getAmethyst_symbols() {
        return amethyst_symbols;
    }

    public void addAmethyst_symbol(Amethyst_symbol amethyst_symbol) {
        this.amethyst_symbols.add(amethyst_symbol);
    }
    public amethyst_ClassDeclaration getAmethyst_classdeclaration() {
        return amethyst_classdeclaration;
    }

    public void setAmethyst_classdeclaration(amethyst_ClassDeclaration amethyst_classdeclaration) {
        this.amethyst_classdeclaration = amethyst_classdeclaration;
    }
    public List<amethyst_Symbol> getAmethyst_symbols() {
        return amethyst_symbols;
    }

    public void addAmethyst_symbol(Amethyst_symbol amethyst_symbol) {
        this.amethyst_symbols.add(amethyst_symbol);
    }
    public amethyst_ClassType getAmethyst_classtype() {
        return amethyst_classtype;
    }

    public void setAmethyst_classtype(amethyst_ClassType amethyst_classtype) {
        this.amethyst_classtype = amethyst_classtype;
    }
    public amethyst_TagDeclaration getAmethyst_tagdeclaration() {
        return amethyst_tagdeclaration;
    }

    public void setAmethyst_tagdeclaration(amethyst_TagDeclaration amethyst_tagdeclaration) {
        this.amethyst_tagdeclaration = amethyst_tagdeclaration;
    }

}