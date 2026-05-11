





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageDefinition extends RepositoryType {

    private String rootElement;
    private String xmlName;
    private String xmlTag;





    private iso20022_SyntaxMessageScheme iso20022_syntaxmessagescheme;




    private List<iso20022_SyntaxMessageScheme> iso20022_syntaxmessageschemes;




    private iso20022_MessageDefinitionIdentifier iso20022_messagedefinitionidentifier;


    public iso20022_MessageDefinition(
        String rootElement,        String xmlName,        String xmlTag    ) {
        super(
        );
        this.rootElement = rootElement;
        this.xmlName = xmlName;
        this.xmlTag = xmlTag;
        this.iso20022_syntaxmessageschemes = new ArrayList<>();
    }

    public iso20022_MessageDefinition(
        String rootElement,        String xmlName,        String xmlTag        ArrayList<iso20022_SyntaxMessageScheme> iso20022_syntaxmessageschemes    ) {
        this.rootElement = rootElement;
        this.xmlName = xmlName;
        this.xmlTag = xmlTag;
        this.iso20022_syntaxmessageschemes = iso20022_syntaxmessageschemes;
    }

    public String getRootelement() {
        return rootElement;
    }

    public void setRootelement(String rootElement) {
        this.rootElement = rootElement;
    }
    public String getXmlname() {
        return xmlName;
    }

    public void setXmlname(String xmlName) {
        this.xmlName = xmlName;
    }
    public String getXmltag() {
        return xmlTag;
    }

    public void setXmltag(String xmlTag) {
        this.xmlTag = xmlTag;
    }

    public iso20022_SyntaxMessageScheme getIso20022_syntaxmessagescheme() {
        return iso20022_syntaxmessagescheme;
    }

    public void setIso20022_syntaxmessagescheme(iso20022_SyntaxMessageScheme iso20022_syntaxmessagescheme) {
        this.iso20022_syntaxmessagescheme = iso20022_syntaxmessagescheme;
    }
    public List<iso20022_SyntaxMessageScheme> getIso20022_syntaxmessageschemes() {
        return iso20022_syntaxmessageschemes;
    }

    public void addIso20022_syntaxmessagescheme(Iso20022_syntaxmessagescheme iso20022_syntaxmessagescheme) {
        this.iso20022_syntaxmessageschemes.add(iso20022_syntaxmessagescheme);
    }
    public iso20022_MessageDefinitionIdentifier getIso20022_messagedefinitionidentifier() {
        return iso20022_messagedefinitionidentifier;
    }

    public void setIso20022_messagedefinitionidentifier(iso20022_MessageDefinitionIdentifier iso20022_messagedefinitionidentifier) {
        this.iso20022_messagedefinitionidentifier = iso20022_messagedefinitionidentifier;
    }

}