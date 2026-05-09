





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlOnexecuteType  {

    private String any;
    private String anyAttribute;
    private String scxmlExecutablecontent;



    public scxml_ScxmlOnexecuteType(
        String any,        String anyAttribute,        String scxmlExecutablecontent    ) {
        this.any = any;
        this.anyAttribute = anyAttribute;
        this.scxmlExecutablecontent = scxmlExecutablecontent;
    }


    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getScxmlexecutablecontent() {
        return scxmlExecutablecontent;
    }

    public void setScxmlexecutablecontent(String scxmlExecutablecontent) {
        this.scxmlExecutablecontent = scxmlExecutablecontent;
    }


}