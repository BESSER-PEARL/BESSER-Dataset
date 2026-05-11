





import java.util.List;
import java.util.ArrayList;

public class dsl_Rest extends Action {

    private String resourcedatafrom;
    private String parentdata;
    private String parentName;
    private String authtoken;
    private String ackdatato;
    private String postdatafrom;
    private String headerdatafrom;
    private String url;
    private String headerdata;
    private String urldata;
    private String method;
    private String ackdata;



    public dsl_Rest(
        String resourcedatafrom,        String parentdata,        String parentName,        String authtoken,        String ackdatato,        String postdatafrom,        String headerdatafrom,        String url,        String headerdata,        String urldata,        String method,        String ackdata    ) {
        super(
        );
        this.resourcedatafrom = resourcedatafrom;
        this.parentdata = parentdata;
        this.parentName = parentName;
        this.authtoken = authtoken;
        this.ackdatato = ackdatato;
        this.postdatafrom = postdatafrom;
        this.headerdatafrom = headerdatafrom;
        this.url = url;
        this.headerdata = headerdata;
        this.urldata = urldata;
        this.method = method;
        this.ackdata = ackdata;
    }


    public String getResourcedatafrom() {
        return resourcedatafrom;
    }

    public void setResourcedatafrom(String resourcedatafrom) {
        this.resourcedatafrom = resourcedatafrom;
    }
    public String getParentdata() {
        return parentdata;
    }

    public void setParentdata(String parentdata) {
        this.parentdata = parentdata;
    }
    public String getParentname() {
        return parentName;
    }

    public void setParentname(String parentName) {
        this.parentName = parentName;
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
    public String getPostdatafrom() {
        return postdatafrom;
    }

    public void setPostdatafrom(String postdatafrom) {
        this.postdatafrom = postdatafrom;
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
    public String getHeaderdata() {
        return headerdata;
    }

    public void setHeaderdata(String headerdata) {
        this.headerdata = headerdata;
    }
    public String getUrldata() {
        return urldata;
    }

    public void setUrldata(String urldata) {
        this.urldata = urldata;
    }
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }
    public String getAckdata() {
        return ackdata;
    }

    public void setAckdata(String ackdata) {
        this.ackdata = ackdata;
    }


}