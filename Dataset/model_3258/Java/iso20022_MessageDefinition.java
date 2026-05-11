





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageDefinition extends RepositoryType {

    private String rootElement;
    private String xmlName;
    private String xmlTag;





    private List<iso20022_MessageChoreography> iso20022_messagechoreographys;




    private iso20022_BusinessArea iso20022_businessarea;




    private iso20022_MessageDefinitionIdentifier iso20022_messagedefinitionidentifier;




    private iso20022_SyntaxMessageScheme iso20022_syntaxmessagescheme;




    private List<iso20022_SyntaxMessageScheme> iso20022_syntaxmessageschemes;




    private iso20022_BusinessArea iso20022_businessarea;




    private iso20022_MessageSet iso20022_messageset;




    private List<iso20022_MessageSet> iso20022_messagesets;




    private iso20022_MessageChoreography iso20022_messagechoreography;


    public iso20022_MessageDefinition(
        String rootElement,        String xmlName,        String xmlTag    ) {
        super(
        );
        this.rootElement = rootElement;
        this.xmlName = xmlName;
        this.xmlTag = xmlTag;
        this.iso20022_messagechoreographys = new ArrayList<>();
        this.iso20022_syntaxmessageschemes = new ArrayList<>();
        this.iso20022_messagesets = new ArrayList<>();
    }

    public iso20022_MessageDefinition(
        String rootElement,        String xmlName,        String xmlTag        ArrayList<iso20022_MessageChoreography> iso20022_messagechoreographys,        ArrayList<iso20022_SyntaxMessageScheme> iso20022_syntaxmessageschemes,        ArrayList<iso20022_MessageSet> iso20022_messagesets    ) {
        this.rootElement = rootElement;
        this.xmlName = xmlName;
        this.xmlTag = xmlTag;
        this.iso20022_messagechoreographys = iso20022_messagechoreographys;
        this.iso20022_syntaxmessageschemes = iso20022_syntaxmessageschemes;
        this.iso20022_messagesets = iso20022_messagesets;
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

    public List<iso20022_MessageChoreography> getIso20022_messagechoreographys() {
        return iso20022_messagechoreographys;
    }

    public void addIso20022_messagechoreography(Iso20022_messagechoreography iso20022_messagechoreography) {
        this.iso20022_messagechoreographys.add(iso20022_messagechoreography);
    }
    public iso20022_BusinessArea getIso20022_businessarea() {
        return iso20022_businessarea;
    }

    public void setIso20022_businessarea(iso20022_BusinessArea iso20022_businessarea) {
        this.iso20022_businessarea = iso20022_businessarea;
    }
    public iso20022_MessageDefinitionIdentifier getIso20022_messagedefinitionidentifier() {
        return iso20022_messagedefinitionidentifier;
    }

    public void setIso20022_messagedefinitionidentifier(iso20022_MessageDefinitionIdentifier iso20022_messagedefinitionidentifier) {
        this.iso20022_messagedefinitionidentifier = iso20022_messagedefinitionidentifier;
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
    public iso20022_BusinessArea getIso20022_businessarea() {
        return iso20022_businessarea;
    }

    public void setIso20022_businessarea(iso20022_BusinessArea iso20022_businessarea) {
        this.iso20022_businessarea = iso20022_businessarea;
    }
    public iso20022_MessageSet getIso20022_messageset() {
        return iso20022_messageset;
    }

    public void setIso20022_messageset(iso20022_MessageSet iso20022_messageset) {
        this.iso20022_messageset = iso20022_messageset;
    }
    public List<iso20022_MessageSet> getIso20022_messagesets() {
        return iso20022_messagesets;
    }

    public void addIso20022_messageset(Iso20022_messageset iso20022_messageset) {
        this.iso20022_messagesets.add(iso20022_messageset);
    }
    public iso20022_MessageChoreography getIso20022_messagechoreography() {
        return iso20022_messagechoreography;
    }

    public void setIso20022_messagechoreography(iso20022_MessageChoreography iso20022_messagechoreography) {
        this.iso20022_messagechoreography = iso20022_messagechoreography;
    }

}