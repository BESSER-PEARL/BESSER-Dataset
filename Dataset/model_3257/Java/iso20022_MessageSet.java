





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageSet extends TopLevelCatalogueEntry {






    private List<iso20022_Syntax> iso20022_syntaxs;




    private List<iso20022_Encoding> iso20022_encodings;




    private iso20022_MessageDefinition iso20022_messagedefinition;




    private iso20022_Encoding iso20022_encoding;




    private List<iso20022_MessageDefinition> iso20022_messagedefinitions;




    private iso20022_Syntax iso20022_syntax;


    public iso20022_MessageSet(
    ) {
        super(
        );
        this.iso20022_syntaxs = new ArrayList<>();
        this.iso20022_encodings = new ArrayList<>();
        this.iso20022_messagedefinitions = new ArrayList<>();
    }

    public iso20022_MessageSet(
        ArrayList<iso20022_Syntax> iso20022_syntaxs,        ArrayList<iso20022_Encoding> iso20022_encodings,        ArrayList<iso20022_MessageDefinition> iso20022_messagedefinitions    ) {
        this.iso20022_syntaxs = iso20022_syntaxs;
        this.iso20022_encodings = iso20022_encodings;
        this.iso20022_messagedefinitions = iso20022_messagedefinitions;
    }


    public List<iso20022_Syntax> getIso20022_syntaxs() {
        return iso20022_syntaxs;
    }

    public void addIso20022_syntax(Iso20022_syntax iso20022_syntax) {
        this.iso20022_syntaxs.add(iso20022_syntax);
    }
    public List<iso20022_Encoding> getIso20022_encodings() {
        return iso20022_encodings;
    }

    public void addIso20022_encoding(Iso20022_encoding iso20022_encoding) {
        this.iso20022_encodings.add(iso20022_encoding);
    }
    public iso20022_MessageDefinition getIso20022_messagedefinition() {
        return iso20022_messagedefinition;
    }

    public void setIso20022_messagedefinition(iso20022_MessageDefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinition = iso20022_messagedefinition;
    }
    public iso20022_Encoding getIso20022_encoding() {
        return iso20022_encoding;
    }

    public void setIso20022_encoding(iso20022_Encoding iso20022_encoding) {
        this.iso20022_encoding = iso20022_encoding;
    }
    public List<iso20022_MessageDefinition> getIso20022_messagedefinitions() {
        return iso20022_messagedefinitions;
    }

    public void addIso20022_messagedefinition(Iso20022_messagedefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinitions.add(iso20022_messagedefinition);
    }
    public iso20022_Syntax getIso20022_syntax() {
        return iso20022_syntax;
    }

    public void setIso20022_syntax(iso20022_Syntax iso20022_syntax) {
        this.iso20022_syntax = iso20022_syntax;
    }

}