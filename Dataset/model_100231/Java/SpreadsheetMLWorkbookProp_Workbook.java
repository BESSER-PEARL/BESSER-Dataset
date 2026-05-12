





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorkbookProp_Workbook  {






    private SmartTagsCollection smarttagscollection;




    private CustomDocumentPropertiesCollection customdocumentpropertiescollection;




    private List<Worksheet> worksheets;


    public SpreadsheetMLWorkbookProp_Workbook(
    ) {
        this.worksheets = new ArrayList<>();
    }

    public SpreadsheetMLWorkbookProp_Workbook(
        ArrayList<Worksheet> worksheets    ) {
        this.worksheets = worksheets;
    }


    public SmartTagsCollection getSmarttagscollection() {
        return smarttagscollection;
    }

    public void setSmarttagscollection(SmartTagsCollection smarttagscollection) {
        this.smarttagscollection = smarttagscollection;
    }
    public CustomDocumentPropertiesCollection getCustomdocumentpropertiescollection() {
        return customdocumentpropertiescollection;
    }

    public void setCustomdocumentpropertiescollection(CustomDocumentPropertiesCollection customdocumentpropertiescollection) {
        this.customdocumentpropertiescollection = customdocumentpropertiescollection;
    }
    public List<Worksheet> getWorksheets() {
        return worksheets;
    }

    public void addWorksheet(Worksheet worksheet) {
        this.worksheets.add(worksheet);
    }

}