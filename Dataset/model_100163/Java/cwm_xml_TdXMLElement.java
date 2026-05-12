





import java.util.List;
import java.util.ArrayList;

public class cwm_xml_TdXMLElement extends Element {

    private String javaType;





    private xml_cwm_EObject xml_cwm_eobject;




    private TdXMLDocument tdxmldocument;




    private TdXMLContent tdxmlcontent;


    public cwm_xml_TdXMLElement(
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

    public xml_cwm_EObject getXml_cwm_eobject() {
        return xml_cwm_eobject;
    }

    public void setXml_cwm_eobject(xml_cwm_EObject xml_cwm_eobject) {
        this.xml_cwm_eobject = xml_cwm_eobject;
    }
    public TdXMLDocument getTdxmldocument() {
        return tdxmldocument;
    }

    public void setTdxmldocument(TdXMLDocument tdxmldocument) {
        this.tdxmldocument = tdxmldocument;
    }
    public TdXMLContent getTdxmlcontent() {
        return tdxmlcontent;
    }

    public void setTdxmlcontent(TdXMLContent tdxmlcontent) {
        this.tdxmlcontent = tdxmlcontent;
    }

}