





import java.util.List;
import java.util.ArrayList;

public class connection_xml_TdXmlSchema extends Schema {

    private String xsdFilePath;



    public connection_xml_TdXmlSchema(
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