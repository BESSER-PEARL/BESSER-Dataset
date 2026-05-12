





import java.util.List;
import java.util.ArrayList;

public class WordprocessingMLBasicDef_CustomDocumentPropertiesCollection  {






    private WordDocument worddocument;




    private List<CustomDocumentProperty> customdocumentpropertys;


    public WordprocessingMLBasicDef_CustomDocumentPropertiesCollection(
    ) {
        this.customdocumentpropertys = new ArrayList<>();
    }

    public WordprocessingMLBasicDef_CustomDocumentPropertiesCollection(
        ArrayList<CustomDocumentProperty> customdocumentpropertys    ) {
        this.customdocumentpropertys = customdocumentpropertys;
    }


    public WordDocument getWorddocument() {
        return worddocument;
    }

    public void setWorddocument(WordDocument worddocument) {
        this.worddocument = worddocument;
    }
    public List<CustomDocumentProperty> getCustomdocumentpropertys() {
        return customdocumentpropertys;
    }

    public void addCustomdocumentproperty(Customdocumentproperty customdocumentproperty) {
        this.customdocumentpropertys.add(customdocumentproperty);
    }

}