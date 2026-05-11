





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_ParameterWithMode extends Parameter {

    private String mode;



    public SQL2003_V2_ParameterWithMode(
        String mode    ) {
        super(
        );
        this.mode = mode;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }


}