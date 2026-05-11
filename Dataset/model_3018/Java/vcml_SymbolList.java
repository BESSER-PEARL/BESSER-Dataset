





import java.util.List;
import java.util.ArrayList;

public class vcml_SymbolList extends List {






    private List<vcml_SymbolicLiteral> vcml_symbolicliterals;


    public vcml_SymbolList(
    ) {
        super(
        );
        this.vcml_symbolicliterals = new ArrayList<>();
    }

    public vcml_SymbolList(
        ArrayList<vcml_SymbolicLiteral> vcml_symbolicliterals    ) {
        this.vcml_symbolicliterals = vcml_symbolicliterals;
    }


    public List<vcml_SymbolicLiteral> getVcml_symbolicliterals() {
        return vcml_symbolicliterals;
    }

    public void addVcml_symbolicliteral(Vcml_symbolicliteral vcml_symbolicliteral) {
        this.vcml_symbolicliterals.add(vcml_symbolicliteral);
    }

}