





import java.util.List;
import java.util.ArrayList;

public class shr5_CommonProgram extends RiggerProgram, MatrixProgram {

    private String programType;



    public shr5_CommonProgram(
        String programType    ) {
        super(
        );
        this.programType = programType;
    }


    public String getProgramtype() {
        return programType;
    }

    public void setProgramtype(String programType) {
        this.programType = programType;
    }


}