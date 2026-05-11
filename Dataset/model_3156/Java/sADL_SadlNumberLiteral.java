





import java.util.List;
import java.util.ArrayList;

public class sADL_SadlNumberLiteral extends SadlExplicitValueLiteral {

    private String unit;
    private String literalNumber;



    public sADL_SadlNumberLiteral(
        String unit,        String literalNumber    ) {
        super(
        );
        this.unit = unit;
        this.literalNumber = literalNumber;
    }


    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getLiteralnumber() {
        return literalNumber;
    }

    public void setLiteralnumber(String literalNumber) {
        this.literalNumber = literalNumber;
    }


}