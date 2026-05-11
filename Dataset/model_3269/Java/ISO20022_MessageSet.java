





import java.util.List;
import java.util.ArrayList;

public class ISO20022_MessageSet extends TopLevelCatalogueEntry {






    private ISO20022_Encoding iso20022_encoding;




    private List<ISO20022_Syntax> iso20022_syntaxs;




    private List<ISO20022_Interaction> iso20022_interactions;




    private List<ISO20022_Encoding> iso20022_encodings;




    private ISO20022_MessageDefinition iso20022_messagedefinition;




    private List<ISO20022_MessageDefinition> iso20022_messagedefinitions;




    private ISO20022_Interaction iso20022_interaction;




    private ISO20022_Syntax iso20022_syntax;


    public ISO20022_MessageSet(
    ) {
        super(
        );
        this.iso20022_syntaxs = new ArrayList<>();
        this.iso20022_interactions = new ArrayList<>();
        this.iso20022_encodings = new ArrayList<>();
        this.iso20022_messagedefinitions = new ArrayList<>();
    }

    public ISO20022_MessageSet(
        ArrayList<ISO20022_Syntax> iso20022_syntaxs,        ArrayList<ISO20022_Interaction> iso20022_interactions,        ArrayList<ISO20022_Encoding> iso20022_encodings,        ArrayList<ISO20022_MessageDefinition> iso20022_messagedefinitions    ) {
        this.iso20022_syntaxs = iso20022_syntaxs;
        this.iso20022_interactions = iso20022_interactions;
        this.iso20022_encodings = iso20022_encodings;
        this.iso20022_messagedefinitions = iso20022_messagedefinitions;
    }


    public ISO20022_Encoding getIso20022_encoding() {
        return iso20022_encoding;
    }

    public void setIso20022_encoding(ISO20022_Encoding iso20022_encoding) {
        this.iso20022_encoding = iso20022_encoding;
    }
    public List<ISO20022_Syntax> getIso20022_syntaxs() {
        return iso20022_syntaxs;
    }

    public void addIso20022_syntax(Iso20022_syntax iso20022_syntax) {
        this.iso20022_syntaxs.add(iso20022_syntax);
    }
    public List<ISO20022_Interaction> getIso20022_interactions() {
        return iso20022_interactions;
    }

    public void addIso20022_interaction(Iso20022_interaction iso20022_interaction) {
        this.iso20022_interactions.add(iso20022_interaction);
    }
    public List<ISO20022_Encoding> getIso20022_encodings() {
        return iso20022_encodings;
    }

    public void addIso20022_encoding(Iso20022_encoding iso20022_encoding) {
        this.iso20022_encodings.add(iso20022_encoding);
    }
    public ISO20022_MessageDefinition getIso20022_messagedefinition() {
        return iso20022_messagedefinition;
    }

    public void setIso20022_messagedefinition(ISO20022_MessageDefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinition = iso20022_messagedefinition;
    }
    public List<ISO20022_MessageDefinition> getIso20022_messagedefinitions() {
        return iso20022_messagedefinitions;
    }

    public void addIso20022_messagedefinition(Iso20022_messagedefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinitions.add(iso20022_messagedefinition);
    }
    public ISO20022_Interaction getIso20022_interaction() {
        return iso20022_interaction;
    }

    public void setIso20022_interaction(ISO20022_Interaction iso20022_interaction) {
        this.iso20022_interaction = iso20022_interaction;
    }
    public ISO20022_Syntax getIso20022_syntax() {
        return iso20022_syntax;
    }

    public void setIso20022_syntax(ISO20022_Syntax iso20022_syntax) {
        this.iso20022_syntax = iso20022_syntax;
    }

}