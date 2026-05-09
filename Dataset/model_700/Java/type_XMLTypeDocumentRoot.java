





import java.util.List;
import java.util.ArrayList;

public class type_XMLTypeDocumentRoot  {

    private String comment;
    private String text;
    private String cDATA;
    private String mixed;





    private List<type_ProcessingInstruction> type_processinginstructions;


    public type_XMLTypeDocumentRoot(
        String comment,        String text,        String cDATA,        String mixed    ) {
        this.comment = comment;
        this.text = text;
        this.cDATA = cDATA;
        this.mixed = mixed;
        this.type_processinginstructions = new ArrayList<>();
    }

    public type_XMLTypeDocumentRoot(
        String comment,        String text,        String cDATA,        String mixed        ArrayList<type_ProcessingInstruction> type_processinginstructions    ) {
        this.comment = comment;
        this.text = text;
        this.cDATA = cDATA;
        this.mixed = mixed;
        this.type_processinginstructions = type_processinginstructions;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getCdata() {
        return cDATA;
    }

    public void setCdata(String cDATA) {
        this.cDATA = cDATA;
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