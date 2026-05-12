





import java.util.List;
import java.util.ArrayList;

public class ASM_MetaInformation extends LocatedElement {

    private String usedAs;



    public ASM_MetaInformation(
        String usedAs    ) {
        super(
        );
        this.usedAs = usedAs;
    }


    public String getUsedas() {
        return usedAs;
    }

    public void setUsedas(String usedAs) {
        this.usedAs = usedAs;
    }


}