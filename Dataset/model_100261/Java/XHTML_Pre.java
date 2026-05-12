





import java.util.List;
import java.util.ArrayList;

public class XHTML_Pre extends Attrs, Blocktext {

    private String xml_space;





    private List<PreContent> precontents;


    public XHTML_Pre(
        String xml_space    ) {
        super(
        );
        this.xml_space = xml_space;
        this.precontents = new ArrayList<>();
    }

    public XHTML_Pre(
        String xml_space        ArrayList<PreContent> precontents    ) {
        this.xml_space = xml_space;
        this.precontents = precontents;
    }

    public String getXml_space() {
        return xml_space;
    }

    public void setXml_space(String xml_space) {
        this.xml_space = xml_space;
    }

    public List<PreContent> getPrecontents() {
        return precontents;
    }

    public void addPrecontent(Precontent precontent) {
        this.precontents.add(precontent);
    }

}