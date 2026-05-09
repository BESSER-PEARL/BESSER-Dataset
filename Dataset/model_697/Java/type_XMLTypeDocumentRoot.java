





import java.util.List;
import java.util.ArrayList;

public class type_XMLTypeDocumentRoot  {

    private String mixed;
    private String comment;
    private String cDATA;
    private String text;





    private List<type_ProcessingInstruction> type_processinginstructions;


    public type_XMLTypeDocumentRoot(
        String mixed,        String comment,        String cDATA,        String text    ) {
        this.mixed = mixed;
        this.comment = comment;
        this.cDATA = cDATA;
        this.text = text;
        this.type_processinginstructions = new ArrayList<>();
    }

    public type_XMLTypeDocumentRoot(
        String mixed,        String comment,        String cDATA,        String text        ArrayList<type_ProcessingInstruction> type_processinginstructions    ) {
        this.mixed = mixed;
        this.comment = comment;
        this.cDATA = cDATA;
        this.text = text;
        this.type_processinginstructions = type_processinginstructions;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
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

    public List<type_ProcessingInstruction> getType_processinginstructions() {
        return type_processinginstructions;
    }

    public void addType_processinginstruction(Type_processinginstruction type_processinginstruction) {
        this.type_processinginstructions.add(type_processinginstruction);
    }

}