





import java.util.List;
import java.util.ArrayList;

public class fmpl_Policy  {

    private String parserURI;
    private String name;



    public fmpl_Policy(
        String parserURI,        String name    ) {
        this.parserURI = parserURI;
        this.name = name;
    }


    public String getParseruri() {
        return parserURI;
    }

    public void setParseruri(String parserURI) {
        this.parserURI = parserURI;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}