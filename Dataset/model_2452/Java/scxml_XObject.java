





import java.util.List;
import java.util.ArrayList;

public class scxml_XObject  {

    private String nsUri;
    private boolean exchange;
    private String classifierName;



    public scxml_XObject(
        String nsUri,        boolean exchange,        String classifierName    ) {
        this.nsUri = nsUri;
        this.exchange = exchange;
        this.classifierName = classifierName;
    }


    public String getNsuri() {
        return nsUri;
    }

    public void setNsuri(String nsUri) {
        this.nsUri = nsUri;
    }
    public boolean getExchange() {
        return exchange;
    }

    public void setExchange(boolean exchange) {
        this.exchange = exchange;
    }
    public String getClassifiername() {
        return classifierName;
    }

    public void setClassifiername(String classifierName) {
        this.classifierName = classifierName;
    }


}