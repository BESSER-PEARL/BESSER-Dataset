





import java.util.List;
import java.util.ArrayList;

public class ClockRDL_literals_ClockLiteral extends Literal {

    private String isInternal;
    private String name;



    public ClockRDL_literals_ClockLiteral(
        String isInternal,        String name    ) {
        super(
        );
        this.isInternal = isInternal;
        this.name = name;
    }


    public String getIsinternal() {
        return isInternal;
    }

    public void setIsinternal(String isInternal) {
        this.isInternal = isInternal;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}