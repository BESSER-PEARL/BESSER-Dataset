





import java.util.List;
import java.util.ArrayList;

public class connection_xml_TdXmlElementType extends ElementType {

    private String javaType;





    private xml_connection_EObject xml_connection_eobject;




    private xml_TdXmlContent xml_tdxmlcontent;




    private xml_TdXmlSchema xml_tdxmlschema;


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

    public xml_connection_EObject getXml_connection_eobject() {
        return xml_connection_eobject;
    }

    public void setXml_connection_eobject(xml_connection_EObject xml_connection_eobject) {
        this.xml_connection_eobject = xml_connection_eobject;
    }
    public xml_TdXmlContent getXml_tdxmlcontent() {
        return xml_tdxmlcontent;
    }

    public void setXml_tdxmlcontent(xml_TdXmlContent xml_tdxmlcontent) {
        this.xml_tdxmlcontent = xml_tdxmlcontent;
    }
    public xml_TdXmlSchema getXml_tdxmlschema() {
        return xml_tdxmlschema;
    }

    public void setXml_tdxmlschema(xml_TdXmlSchema xml_tdxmlschema) {
        this.xml_tdxmlschema = xml_tdxmlschema;
    }

}