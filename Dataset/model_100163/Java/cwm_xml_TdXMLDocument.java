





import java.util.List;
import java.util.ArrayList;

public class cwm_xml_TdXMLDocument extends Document {

    private String xsdFilePath;



    public cwm_xml_TdXMLDocument(
        String xsdFilePath    ) {
        super(
        );
        this.xsdFilePath = xsdFilePath;
    }


    public String getXsdfilepath() {
        return xsdFilePath;
    }

    public void setXsdfilepath(String xsdFilePath) {
        this.xsdFilePath = xsdFilePath;
    }


}