





import java.util.List;
import java.util.ArrayList;

public class type_XMLTypeDocumentRoot  {

    private String cDATA;
    private String text;
    private String comment;
    private String mixed;





    private List<type_ProcessingInstruction> type_processinginstructions;


    public type_XMLTypeDocumentRoot(
        String cDATA,        String text,        String comment,        String mixed    ) {
        this.cDATA = cDATA;
        this.text = text;
        this.comment = comment;
        this.mixed = mixed;
        this.type_processinginstructions = new ArrayList<>();
    }

    public type_XMLTypeDocumentRoot(
        String cDATA,        String text,        String comment,        String mixed        ArrayList<type_ProcessingInstruction> type_processinginstructions    ) {
        this.cDATA = cDATA;
        this.text = text;
        this.comment = comment;
        this.mixed = mixed;
        this.type_processinginstructions = type_processinginstructions;
    }

    public String getCdata() {
        return cDATA;
    }

    public void setCdata(String cDATA) {
        this.cDATA = cDATA;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<type_ProcessingInstruction> getType_processinginstructions() {
        return type_processinginstructions;
    }

    public void addType_processinginstruction(Type_processinginstruction type_processinginstruction) {
        this.type_processinginstructions.add(type_processinginstruction);
    }

}