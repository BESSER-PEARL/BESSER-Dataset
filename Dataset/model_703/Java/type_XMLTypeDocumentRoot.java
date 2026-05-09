





import java.util.List;
import java.util.ArrayList;

public class type_XMLTypeDocumentRoot  {

    private String text;
    private String cDATA;
    private String mixed;
    private String comment;





    private List<type_ProcessingInstruction> type_processinginstructions;


    public type_XMLTypeDocumentRoot(
        String text,        String cDATA,        String mixed,        String comment    ) {
        this.text = text;
        this.cDATA = cDATA;
        this.mixed = mixed;
        this.comment = comment;
        this.type_processinginstructions = new ArrayList<>();
    }

    public type_XMLTypeDocumentRoot(
        String text,        String cDATA,        String mixed,        String comment        ArrayList<type_ProcessingInstruction> type_processinginstructions    ) {
        this.text = text;
        this.cDATA = cDATA;
        this.mixed = mixed;
        this.comment = comment;
        this.type_processinginstructions = type_processinginstructions;
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
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public List<type_ProcessingInstruction> getType_processinginstructions() {
        return type_processinginstructions;
    }

    public void addType_processinginstruction(Type_processinginstruction type_processinginstruction) {
        this.type_processinginstructions.add(type_processinginstruction);
    }

}