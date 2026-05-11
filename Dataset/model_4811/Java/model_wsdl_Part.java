





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_Part extends wsdl_IPart, wsdl_ExtensibleElement {

    private String name;
    private String elementName;
    private String typeName;





    private Message message;




    private XSDTypeDefinition xsdtypedefinition;




    private XSDElementDeclaration xsdelementdeclaration;


    public model_wsdl_Part(
        String name,        String elementName,        String typeName    ) {
        super(
        );
        this.name = name;
        this.elementName = elementName;
        this.typeName = typeName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getElementname() {
        return elementName;
    }

    public void setElementname(String elementName) {
        this.elementName = elementName;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }

    public Message getMessage() {
        return message;
    }

    public void setMessage(Message message) {
        this.message = message;
    }
    public XSDTypeDefinition getXsdtypedefinition() {
        return xsdtypedefinition;
    }

    public void setXsdtypedefinition(XSDTypeDefinition xsdtypedefinition) {
        this.xsdtypedefinition = xsdtypedefinition;
    }
    public XSDElementDeclaration getXsdelementdeclaration() {
        return xsdelementdeclaration;
    }

    public void setXsdelementdeclaration(XSDElementDeclaration xsdelementdeclaration) {
        this.xsdelementdeclaration = xsdelementdeclaration;
    }

}