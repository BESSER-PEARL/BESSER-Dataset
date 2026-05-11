





import java.util.List;
import java.util.ArrayList;

public class KM3_Enumeration extends Classifier {






    private KM3_EnumLiteral km3_enumliteral;




    private List<KM3_EnumLiteral> km3_enumliterals;


    public KM3_Enumeration(
    ) {
        super(
        );
        this.km3_enumliterals = new ArrayList<>();
    }

    public KM3_Enumeration(
        ArrayList<KM3_EnumLiteral> km3_enumliterals    ) {
        this.km3_enumliterals = km3_enumliterals;
    }


    public KM3_EnumLiteral getKm3_enumliteral() {
        return km3_enumliteral;
    }

    public void setKm3_enumliteral(KM3_EnumLiteral km3_enumliteral) {
        this.km3_enumliteral = km3_enumliteral;
    }
    public List<KM3_EnumLiteral> getKm3_enumliterals() {
        return km3_enumliterals;
    }

    public void addKm3_enumliteral(Km3_enumliteral km3_enumliteral) {
        this.km3_enumliterals.add(km3_enumliteral);
    }

}