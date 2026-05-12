





import java.util.List;
import java.util.ArrayList;

public class sml_EnumRanges extends AbstractRanges {






    private List<sml_SmlEEnumLiteral> sml_smleenumliterals;


    public sml_EnumRanges(
    ) {
        super(
        );
        this.sml_smleenumliterals = new ArrayList<>();
    }

    public sml_EnumRanges(
        ArrayList<sml_SmlEEnumLiteral> sml_smleenumliterals    ) {
        this.sml_smleenumliterals = sml_smleenumliterals;
    }


    public List<sml_SmlEEnumLiteral> getSml_smleenumliterals() {
        return sml_smleenumliterals;
    }

    public void addSml_smleenumliteral(Sml_smleenumliteral sml_smleenumliteral) {
        this.sml_smleenumliterals.add(sml_smleenumliteral);
    }

}