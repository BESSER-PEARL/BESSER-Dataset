





import java.util.List;
import java.util.ArrayList;

public class connection_xml_TdXmlElementType extends ElementType {

    private String javaType;





    private xml_TdXmlContent xml_tdxmlcontent;


    public connection_xml_TdXmlElementType(
        String javaType    ) {
        super(
        );
        this.javaType = javaType;
    }


    public String getJavatype() {
        return javaType;
    }

    public void setJavatype(String javaType) {
        this.javaType = javaType;
    }

    public xml_TdXmlContent getXml_tdxmlcontent() {
        return xml_tdxmlcontent;
    }

    public void setXml_tdxmlcontent(xml_TdXmlContent xml_tdxmlcontent) {
        this.xml_tdxmlcontent = xml_tdxmlcontent;
    }

}