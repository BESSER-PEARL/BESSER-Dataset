





import java.util.List;
import java.util.ArrayList;

public class ORDB4ORA_OperationParameter extends Parameter {

    private String Mode;



    public ORDB4ORA_OperationParameter(
        String Mode    ) {
        super(
        );
        this.Mode = Mode;
    }


    public String getMode() {
        return Mode;
    }

    public void setMode(String Mode) {
        this.Mode = Mode;
    }


}