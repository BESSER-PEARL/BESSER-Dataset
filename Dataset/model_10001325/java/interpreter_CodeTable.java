





import java.util.List;
import java.util.ArrayList;

public class interpreter_CodeTable  {

    private String codeMap;
    private String byteCodesTXT;



    public interpreter_CodeTable(
        String codeMap,        String byteCodesTXT    ) {
        this.codeMap = codeMap;
        this.byteCodesTXT = byteCodesTXT;
    }


    public String getCodemap() {
        return codeMap;
    }

    public void setCodemap(String codeMap) {
        this.codeMap = codeMap;
    }
    public String getBytecodestxt() {
        return byteCodesTXT;
    }

    public void setBytecodestxt(String byteCodesTXT) {
        this.byteCodesTXT = byteCodesTXT;
    }


}