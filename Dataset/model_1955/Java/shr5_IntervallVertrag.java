





import java.util.List;
import java.util.ArrayList;

public class shr5_IntervallVertrag extends Vertrag {

    private int faelligkeitsIntervall;
    private String begin;
    private String unit;



    public shr5_IntervallVertrag(
        int faelligkeitsIntervall,        String begin,        String unit    ) {
        super(
        );
        this.faelligkeitsIntervall = faelligkeitsIntervall;
        this.begin = begin;
        this.unit = unit;
    }


    public int getFaelligkeitsintervall() {
        return faelligkeitsIntervall;
    }

    public void setFaelligkeitsintervall(int faelligkeitsIntervall) {
        this.faelligkeitsIntervall = faelligkeitsIntervall;
    }
    public String getBegin() {
        return begin;
    }

    public void setBegin(String begin) {
        this.begin = begin;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }


}