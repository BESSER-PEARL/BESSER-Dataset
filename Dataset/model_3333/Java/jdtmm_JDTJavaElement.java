





import java.util.List;
import java.util.ArrayList;

public class jdtmm_JDTJavaElement  {

    private String elementName;
    private String comment;
    private String elementType;
    private String generated;



    public jdtmm_JDTJavaElement(
        String elementName,        String comment,        String elementType,        String generated    ) {
        this.elementName = elementName;
        this.comment = comment;
        this.elementType = elementType;
        this.generated = generated;
    }


    public String getElementname() {
        return elementName;
    }

    public void setElementname(String elementName) {
        this.elementName = elementName;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getElementtype() {
        return elementType;
    }

    public void setElementtype(String elementType) {
        this.elementType = elementType;
    }
    public String getGenerated() {
        return generated;
    }

    public void setGenerated(String generated) {
        this.generated = generated;
    }


}