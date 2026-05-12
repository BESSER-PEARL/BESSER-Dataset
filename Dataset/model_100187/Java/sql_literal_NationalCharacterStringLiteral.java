





import java.util.List;
import java.util.ArrayList;

public class sql_literal_NationalCharacterStringLiteral extends GeneralLiteral {

    private String values;





    private List<Separator> separators;


    public sql_literal_NationalCharacterStringLiteral(
        String values    ) {
        super(
        );
        this.values = values;
        this.separators = new ArrayList<>();
    }

    public sql_literal_NationalCharacterStringLiteral(
        String values        ArrayList<Separator> separators    ) {
        this.values = values;
        this.separators = separators;
    }

    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }

    public List<Separator> getSeparators() {
        return separators;
    }

    public void addSeparator(Separator separator) {
        this.separators.add(separator);
    }

}