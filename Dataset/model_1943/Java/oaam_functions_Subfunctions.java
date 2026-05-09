





import java.util.List;
import java.util.ArrayList;

public class oaam_functions_Subfunctions extends FunctionsContainerA {

    private int multiplicityMin;
    private int multiplicityMax;



    public oaam_functions_Subfunctions(
        int multiplicityMin,        int multiplicityMax    ) {
        super(
        );
        this.multiplicityMin = multiplicityMin;
        this.multiplicityMax = multiplicityMax;
    }


    public int getMultiplicitymin() {
        return multiplicityMin;
    }

    public void setMultiplicitymin(int multiplicityMin) {
        this.multiplicityMin = multiplicityMin;
    }
    public int getMultiplicitymax() {
        return multiplicityMax;
    }

    public void setMultiplicitymax(int multiplicityMax) {
        this.multiplicityMax = multiplicityMax;
    }


}