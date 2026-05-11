





import java.util.List;
import java.util.ArrayList;

public class MARTE_Time_TimedValueSpecification extends TimedElement {

    private String interpretation;



    public MARTE_Time_TimedValueSpecification(
        String interpretation    ) {
        super(
        );
        this.interpretation = interpretation;
    }


    public String getInterpretation() {
        return interpretation;
    }

    public void setInterpretation(String interpretation) {
        this.interpretation = interpretation;
    }


}