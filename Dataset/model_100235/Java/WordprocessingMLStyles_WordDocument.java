





import java.util.List;
import java.util.ArrayList;

public class WordprocessingMLStyles_WordDocument  {






    private ListsElt listselt;




    private StringProperty stringproperty;




    private DocumentPropertiesCollection documentpropertiescollection;




    private StringProperty stringproperty;




    private SmartTagsCollection smarttagscollection;




    private FontsListElt fontslistelt;




    private CustomDocumentPropertiesCollection customdocumentpropertiescollection;


    public WordprocessingMLStyles_WordDocument(
    ) {
        this.listselts = new ArrayList<>();
    }



    public ListsElt getListselts() {
        return listselts;
    }

    public void addListselt(Listselt listselt) {
        this.listselts.add(listselt);
    }
    public StringProperty getStringproperty() {
        return stringproperty;
    }

    public void setStringproperty(StringProperty stringproperty) {
        this.stringproperty = stringproperty;
    }
    public DocumentPropertiesCollection getDocumentpropertiescollection() {
        return documentpropertiescollection;
    }

    public void setDocumentpropertiescollection(DocumentPropertiesCollection documentpropertiescollection) {
        this.documentpropertiescollection = documentpropertiescollection;
    }
    public StringProperty getStringproperty() {
        return stringproperty;
    }

    public void setStringproperty(StringProperty stringproperty) {
        this.stringproperty = stringproperty;
    }
    public SmartTagsCollection getSmarttagscollection() {
        return smarttagscollection;
    }

    public void setSmarttagscollection(SmartTagsCollection smarttagscollection) {
        this.smarttagscollection = smarttagscollection;
    }
    public FontsListElt getFontslistelt() {
        return fontslistelt;
    }

    public void setFontslistelt(FontsListElt fontslistelt) {
        this.fontslistelt = fontslistelt;
    }
    public CustomDocumentPropertiesCollection getCustomdocumentpropertiescollection() {
        return customdocumentpropertiescollection;
    }

    public void setCustomdocumentpropertiescollection(CustomDocumentPropertiesCollection customdocumentpropertiescollection) {
        this.customdocumentpropertiescollection = customdocumentpropertiescollection;
    }

}