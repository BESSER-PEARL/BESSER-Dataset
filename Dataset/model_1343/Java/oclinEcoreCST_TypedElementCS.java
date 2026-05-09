





import java.util.List;
import java.util.ArrayList;

public class oclinEcoreCST_TypedElementCS extends NamedElementCS {

    private String qualifiers;
    private int lower;
    private int upper;
    private String multiplicity;



    public oclinEcoreCST_TypedElementCS(
        String qualifiers,        int lower,        int upper,        String multiplicity    ) {
        super(
        );
        this.qualifiers = qualifiers;
        this.lower = lower;
        this.upper = upper;
        this.multiplicity = multiplicity;
    }


    public String getQualifiers() {
        return qualifiers;
    }

    public void setQualifiers(String qualifiers) {
        this.qualifiers = qualifiers;
    }
    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public String getMultiplicity() {
        return multiplicity;
    }

    public void setMultiplicity(String multiplicity) {
        this.multiplicity = multiplicity;
    }


}