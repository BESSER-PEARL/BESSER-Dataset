





import java.util.List;
import java.util.ArrayList;

public class libraryElement_CompilerInfo  {

    private String classdef;
    private String header;



    public libraryElement_CompilerInfo(
        String classdef,        String header    ) {
        this.classdef = classdef;
        this.header = header;
    }


    public String getClassdef() {
        return classdef;
    }

    public void setClassdef(String classdef) {
        this.classdef = classdef;
    }
    public String getHeader() {
        return header;
    }

    public void setHeader(String header) {
        this.header = header;
    }


}