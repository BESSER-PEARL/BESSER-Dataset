





import java.util.List;
import java.util.ArrayList;

public class model_xsd_XSDNamedComponent extends XSDComponent {

    private String name;
    private String qName;
    private String aliasName;
    private String uRI;
    private String aliasURI;
    private String targetNamespace;



    public model_xsd_XSDNamedComponent(
        String name,        String qName,        String aliasName,        String uRI,        String aliasURI,        String targetNamespace    ) {
        super(
        );
        this.name = name;
        this.qName = qName;
        this.aliasName = aliasName;
        this.uRI = uRI;
        this.aliasURI = aliasURI;
        this.targetNamespace = targetNamespace;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getQname() {
        return qName;
    }

    public void setQname(String qName) {
        this.qName = qName;
    }
    public String getAliasname() {
        return aliasName;
    }

    public void setAliasname(String aliasName) {
        this.aliasName = aliasName;
    }
    public String getUri() {
        return uRI;
    }

    public void setUri(String uRI) {
        this.uRI = uRI;
    }
    public String getAliasuri() {
        return aliasURI;
    }

    public void setAliasuri(String aliasURI) {
        this.aliasURI = aliasURI;
    }
    public String getTargetnamespace() {
        return targetNamespace;
    }

    public void setTargetnamespace(String targetNamespace) {
        this.targetNamespace = targetNamespace;
    }


}