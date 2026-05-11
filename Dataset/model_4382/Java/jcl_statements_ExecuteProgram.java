





import java.util.List;
import java.util.ArrayList;

public class jcl_statements_ExecuteProgram extends Execute {

    private String programName;



    public jcl_statements_ExecuteProgram(
        String programName    ) {
        super(
        );
        this.programName = programName;
    }


    public String getProgramname() {
        return programName;
    }

    public void setProgramname(String programName) {
        this.programName = programName;
    }


}