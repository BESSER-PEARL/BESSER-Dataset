





import java.util.List;
import java.util.ArrayList;

public class sparrow_Rest extends Action {

    private String parentName;
    private String ackdata;
    private String method;
    private String headerdata;
    private String resourcedatafrom;
    private String urldata;
    private String authtoken;
    private String ackdatato;
    private String headerdatafrom;
    private String url;
    private String parentdata;
    private String postdatafrom;



    public sparrow_Rest(
        String parentName,        String ackdata,        String method,        String headerdata,        String resourcedatafrom,        String urldata,        String authtoken,        String ackdatato,        String headerdatafrom,        String url,        String parentdata,        String postdatafrom    ) {
        super(
        );
        this.parentName = parentName;
        this.ackdata = ackdata;
        this.method = method;
        this.headerdata = headerdata;
        this.resourcedatafrom = resourcedatafrom;
        this.urldata = urldata;
        this.authtoken = authtoken;
        this.ackdatato = ackdatato;
        this.headerdatafrom = headerdatafrom;
        this.url = url;
        this.parentdata = parentdata;
        this.postdatafrom = postdatafrom;
    }


    public String getParentname() {
        return parentName;
    }

    public void setParentname(String parentName) {
        this.parentName = parentName;
    }
    public String getAckdata() {
        return ackdata;
    }

    public void setAckdata(String ackdata) {
        this.ackdata = ackdata;
    }
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }
    public String getHeaderdata() {
        return headerdata;
    }

    public void setHeaderdata(String headerdata) {
        this.headerdata = headerdata;
    }
    public String getResourcedatafrom() {
        return resourcedatafrom;
    }

    public void setResourcedatafrom(String resourcedatafrom) {
        this.resourcedatafrom = resourcedatafrom;
    }
    public String getUrldata() {
        return urldata;
    }

    public void setUrldata(String urldata) {
        this.urldata = urldata;
    }
    public String getAuthtoken() {
        return authtoken;
    }

    public void setAuthtoken(String authtoken) {
        this.authtoken = authtoken;
    }
    public String getAckdatato() {
        return ackdatato;
    }

    public void setAckdatato(String ackdatato) {
        this.ackdatato = ackdatato;
    }
    public String getHeaderdatafrom() {
        return headerdatafrom;
    }

    public void setHeaderdatafrom(String headerdatafrom) {
        this.headerdatafrom = headerdatafrom;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getParentdata() {
        return parentdata;
    }

    public void setParentdata(String parentdata) {
        this.parentdata = parentdata;
    }
    public String getPostdatafrom() {
        return postdatafrom;
    }

    public void setPostdatafrom(String postdatafrom) {
        this.postdatafrom = postdatafrom;
    }


}