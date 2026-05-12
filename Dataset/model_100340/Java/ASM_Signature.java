





import java.util.List;
import java.util.ArrayList;

public class ASM_Signature extends LocatedElement {

    private String isMain;
    private String name;



    public ASM_Signature(
        String isMain,        String name    ) {
        super(
        );
        this.isMain = isMain;
        this.name = name;
    }


    public String getIsmain() {
        return isMain;
    }

    public void setIsmain(String isMain) {
        this.isMain = isMain;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}