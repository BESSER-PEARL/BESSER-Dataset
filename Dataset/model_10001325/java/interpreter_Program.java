





import java.util.List;
import java.util.ArrayList;

public class interpreter_Program  {

    private String byteCodeVector;
    private String programMap;



    public interpreter_Program(
        String byteCodeVector,        String programMap    ) {
        this.byteCodeVector = byteCodeVector;
        this.programMap = programMap;
    }


    public String getBytecodevector() {
        return byteCodeVector;
    }

    public void setBytecodevector(String byteCodeVector) {
        this.byteCodeVector = byteCodeVector;
    }
    public String getProgrammap() {
        return programMap;
    }

    public void setProgrammap(String programMap) {
        this.programMap = programMap;
    }


}