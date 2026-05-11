





import java.util.List;
import java.util.ArrayList;

public class SPL_Dialog extends Session {






    private List<SPL_Method> spl_methods;




    private List<SPL_Declaration> spl_declarations;


    public SPL_Dialog(
    ) {
        super(
        );
        this.spl_methods = new ArrayList<>();
        this.spl_declarations = new ArrayList<>();
    }

    public SPL_Dialog(
        ArrayList<SPL_Method> spl_methods,        ArrayList<SPL_Declaration> spl_declarations    ) {
        this.spl_methods = spl_methods;
        this.spl_declarations = spl_declarations;
    }


    public List<SPL_Method> getSpl_methods() {
        return spl_methods;
    }

    public void addSpl_method(Spl_method spl_method) {
        this.spl_methods.add(spl_method);
    }
    public List<SPL_Declaration> getSpl_declarations() {
        return spl_declarations;
    }

    public void addSpl_declaration(Spl_declaration spl_declaration) {
        this.spl_declarations.add(spl_declaration);
    }

}