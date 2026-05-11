





import java.util.List;
import java.util.ArrayList;

public class vcml_SymbolicType extends CharacteristicType {

    private boolean caseSensitive;



    public vcml_SymbolicType(
        boolean caseSensitive    ) {
        super(
        );
        this.caseSensitive = caseSensitive;
    }


    public boolean getCasesensitive() {
        return caseSensitive;
    }

    public void setCasesensitive(boolean caseSensitive) {
        this.caseSensitive = caseSensitive;
    }


}