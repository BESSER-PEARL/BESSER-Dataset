





import java.util.List;
import java.util.ArrayList;

public class Interpreter_ByteCodeLoader  {

    private String byteSource;
    private String byteCodeList;
    private String program;



    public Interpreter_ByteCodeLoader(
        String byteSource,        String byteCodeList,        String program    ) {
        this.byteSource = byteSource;
        this.byteCodeList = byteCodeList;
        this.program = program;
    }


    public String getBytesource() {
        return byteSource;
    }

    public void setBytesource(String byteSource) {
        this.byteSource = byteSource;
    }
    public String getBytecodelist() {
        return byteCodeList;
    }

    public void setBytecodelist(String byteCodeList) {
        this.byteCodeList = byteCodeList;
    }
    public String getProgram() {
        return program;
    }

    public void setProgram(String program) {
        this.program = program;
    }


}