





import java.util.List;
import java.util.ArrayList;

public class common_Identifiable  {

    private String typeURI;
    private String uRI;





    private common_DublinCore common_dublincore;


    public common_Identifiable(
        String typeURI,        String uRI    ) {
        this.typeURI = typeURI;
        this.uRI = uRI;
    }


    public String getTypeuri() {
        return typeURI;
    }

    public void setTypeuri(String typeURI) {
        this.typeURI = typeURI;
    }
    public String getUri() {
        return uRI;
    }

    public void setUri(String uRI) {
        this.uRI = uRI;
    }

    public common_DublinCore getCommon_dublincore() {
        return common_dublincore;
    }

    public void setCommon_dublincore(common_DublinCore common_dublincore) {
        this.common_dublincore = common_dublincore;
    }

}