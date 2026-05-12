





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLBasicDef_Workbook  {






    private List<Worksheet> worksheets;




    private CustomDocumentPropertiesCollection customdocumentpropertiescollection;




    private DocumentPropertiesCollection documentpropertiescollection;




    private SmartTagsCollection smarttagscollection;


    public SpreadsheetMLBasicDef_Workbook(
    ) {
        this.worksheets = new ArrayList<>();
    }

    public SpreadsheetMLBasicDef_Workbook(
        ArrayList<Worksheet> worksheets    ) {
        this.worksheets = worksheets;
    }


    public List<Worksheet> getWorksheets() {
        return worksheets;
    }

    public void addWorksheet(Worksheet worksheet) {
        this.worksheets.add(worksheet);
    }
    public CustomDocumentPropertiesCollection getCustomdocumentpropertiescollection() {
        return customdocumentpropertiescollection;
    }

    public void setCustomdocumentpropertiescollection(CustomDocumentPropertiesCollection customdocumentpropertiescollection) {
        this.customdocumentpropertiescollection = customdocumentpropertiescollection;
    }
    public DocumentPropertiesCollection getDocumentpropertiescollection() {
        return documentpropertiescollection;
    }

    public void setDocumentpropertiescollection(DocumentPropertiesCollection documentpropertiescollection) {
        this.documentpropertiescollection = documentpropertiescollection;
    }
    public SmartTagsCollection getSmarttagscollection() {
        return smarttagscollection;
    }

    public void setSmarttagscollection(SmartTagsCollection smarttagscollection) {
        this.smarttagscollection = smarttagscollection;
    }

}