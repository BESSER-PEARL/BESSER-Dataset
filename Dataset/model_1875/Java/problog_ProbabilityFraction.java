





import java.util.List;
import java.util.ArrayList;

public class problog_ProbabilityFraction extends ProbabilityMeasure {

    private int nominator;
    private int denominator;



    public problog_ProbabilityFraction(
        int nominator,        int denominator    ) {
        super(
        );
        this.nominator = nominator;
        this.denominator = denominator;
    }


    public int getNominator() {
        return nominator;
    }

    public void setNominator(int nominator) {
        this.nominator = nominator;
    }
    public int getDenominator() {
        return denominator;
    }

    public void setDenominator(int denominator) {
        this.denominator = denominator;
    }


}