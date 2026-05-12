





import java.util.List;
import java.util.ArrayList;

public class ASM_Rule extends LocatedElement {

    private String inSequence;



    public ASM_Rule(
        String inSequence    ) {
        super(
        );
        this.inSequence = inSequence;
    }


    public String getInsequence() {
        return inSequence;
    }

    public void setInsequence(String inSequence) {
        this.inSequence = inSequence;
    }


}