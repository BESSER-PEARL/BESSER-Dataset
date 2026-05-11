





import java.util.List;
import java.util.ArrayList;

public class idl_ArrayDeclarator extends ComplexDeclarator, Declarator {






    private List<idl_ConstExp> idl_constexps;


    public idl_ArrayDeclarator(
    ) {
        super(
        );
        this.idl_constexps = new ArrayList<>();
    }

    public idl_ArrayDeclarator(
        ArrayList<idl_ConstExp> idl_constexps    ) {
        this.idl_constexps = idl_constexps;
    }


    public List<idl_ConstExp> getIdl_constexps() {
        return idl_constexps;
    }

    public void addIdl_constexp(Idl_constexp idl_constexp) {
        this.idl_constexps.add(idl_constexp);
    }

}