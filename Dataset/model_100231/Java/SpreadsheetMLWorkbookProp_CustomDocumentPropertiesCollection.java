





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection  {






    private Workbook workbook;




    private List<CustomDocumentProperty> customdocumentpropertys;


    public SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection(
    ) {
        this.customdocumentpropertys = new ArrayList<>();
    }

    public SpreadsheetMLWorkbookProp_CustomDocumentPropertiesCollection(
        ArrayList<CustomDocumentProperty> customdocumentpropertys    ) {
        this.customdocumentpropertys = customdocumentpropertys;
    }


    public Workbook getWorkbook() {
        return workbook;
    }

    public void setWorkbook(Workbook workbook) {
        this.workbook = workbook;
    }
    public List<CustomDocumentProperty> getCustomdocumentpropertys() {
        return customdocumentpropertys;
    }

    public void addCustomdocumentproperty(Customdocumentproperty customdocumentproperty) {
        this.customdocumentpropertys.add(customdocumentproperty);
    }

}