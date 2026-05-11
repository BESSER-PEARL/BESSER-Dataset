





import java.util.List;
import java.util.ArrayList;

public class diva_EnumVariable extends Variable {






    private List<diva_EnumLiteral> diva_enumliterals;


    public diva_EnumVariable(
    ) {
        super(
        );
        this.diva_enumliterals = new ArrayList<>();
    }

    public diva_EnumVariable(
        ArrayList<diva_EnumLiteral> diva_enumliterals    ) {
        this.diva_enumliterals = diva_enumliterals;
    }


    public List<diva_EnumLiteral> getDiva_enumliterals() {
        return diva_enumliterals;
    }

    public void addDiva_enumliteral(Diva_enumliteral diva_enumliteral) {
        this.diva_enumliterals.add(diva_enumliteral);
    }

}