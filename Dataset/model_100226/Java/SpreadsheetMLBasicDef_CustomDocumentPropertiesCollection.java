





import java.util.List;
import java.util.ArrayList;

public class SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection  {






    private Workbook workbook;




    private List<CustomDocumentProperty> customdocumentpropertys;


    public SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection(
    ) {
        this.customdocumentpropertys = new ArrayList<>();
    }

    public SpreadsheetMLBasicDef_CustomDocumentPropertiesCollection(
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