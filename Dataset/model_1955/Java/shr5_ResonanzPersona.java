





import java.util.List;
import java.util.ArrayList;

public class shr5_ResonanzPersona extends ActiveMatixDevice {

    private int resonanz;
    private int resonanzBasis;



    public shr5_ResonanzPersona(
        int resonanz,        int resonanzBasis    ) {
        super(
        );
        this.resonanz = resonanz;
        this.resonanzBasis = resonanzBasis;
    }


    public int getResonanz() {
        return resonanz;
    }

    public void setResonanz(int resonanz) {
        this.resonanz = resonanz;
    }
    public int getResonanzbasis() {
        return resonanzBasis;
    }

    public void setResonanzbasis(int resonanzBasis) {
        this.resonanzBasis = resonanzBasis;
    }


}