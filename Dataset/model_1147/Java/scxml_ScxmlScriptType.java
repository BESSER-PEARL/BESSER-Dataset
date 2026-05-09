





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlScriptType  {

    private String any;
    private String scxmlExtraContent;
    private String src;
    private String content;
    private String mixed;





    private scxml_ScxmlOnexecuteType scxml_scxmlonexecutetype;


    public scxml_ScxmlScriptType(
        String any,        String scxmlExtraContent,        String src,        String content,        String mixed    ) {
        this.any = any;
        this.scxmlExtraContent = scxmlExtraContent;
        this.src = src;
        this.content = content;
        this.mixed = mixed;
    }


    public String getAny() {
        return any;
    }

    public void setAny(String any) {
        this.any = any;
    }
    public String getScxmlextracontent() {
        return scxmlExtraContent;
    }

    public void setScxmlextracontent(String scxmlExtraContent) {
        this.scxmlExtraContent = scxmlExtraContent;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public scxml_ScxmlOnexecuteType getScxml_scxmlonexecutetype() {
        return scxml_scxmlonexecutetype;
    }

    public void setScxml_scxmlonexecutetype(scxml_ScxmlOnexecuteType scxml_scxmlonexecutetype) {
        this.scxml_scxmlonexecutetype = scxml_scxmlonexecutetype;
    }

}