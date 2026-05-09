





import java.util.List;
import java.util.ArrayList;

public class JDTAST_WildcardType extends Type {

    private String upperBound;





    private JDTAST_Type jdtast_type;


    public JDTAST_WildcardType(
        String upperBound    ) {
        super(
        );
        this.upperBound = upperBound;
    }


    public String getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(String upperBound) {
        this.upperBound = upperBound;
    }

    public JDTAST_Type getJdtast_type() {
        return jdtast_type;
    }

    public void setJdtast_type(JDTAST_Type jdtast_type) {
        this.jdtast_type = jdtast_type;
    }

}