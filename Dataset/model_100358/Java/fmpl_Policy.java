





import java.util.List;
import java.util.ArrayList;

public class fmpl_Policy  {

    private String name;
    private String parserURI;



    public fmpl_Policy(
        String name,        String parserURI    ) {
        this.name = name;
        this.parserURI = parserURI;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getParseruri() {
        return parserURI;
    }

    public void setParseruri(String parserURI) {
        this.parserURI = parserURI;
    }


}