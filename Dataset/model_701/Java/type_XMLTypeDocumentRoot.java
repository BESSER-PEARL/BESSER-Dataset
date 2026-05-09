





import java.util.List;
import java.util.ArrayList;

public class type_XMLTypeDocumentRoot  {

    private String comment;
    private String mixed;
    private String text;
    private String cDATA;





    private List<type_ProcessingInstruction> type_processinginstructions;


    public type_XMLTypeDocumentRoot(
        String comment,        String mixed,        String text,        String cDATA    ) {
        this.comment = comment;
        this.mixed = mixed;
        this.text = text;
        this.cDATA = cDATA;
        this.type_processinginstructions = new ArrayList<>();
    }

    public type_XMLTypeDocumentRoot(
        String comment,        String mixed,        String text,        String cDATA        ArrayList<type_ProcessingInstruction> type_processinginstructions    ) {
        this.comment = comment;
        this.mixed = mixed;
        this.text = text;
        this.cDATA = cDATA;
        this.type_processinginstructions = type_processinginstructions;
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

    public List<type_ProcessingInstruction> getType_processinginstructions() {
        return type_processinginstructions;
    }

    public void addType_processinginstruction(Type_processinginstruction type_processinginstruction) {
        this.type_processinginstructions.add(type_processinginstruction);
    }

}