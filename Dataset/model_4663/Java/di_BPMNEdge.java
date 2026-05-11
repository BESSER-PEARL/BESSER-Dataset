





import java.util.List;
import java.util.ArrayList;

public class di_BPMNEdge extends LabeledEdge {

    private String messageVisibleKind;





    private di_DocumentRoot di_documentroot;


    public di_BPMNEdge(
        String messageVisibleKind    ) {
        super(
        );
        this.messageVisibleKind = messageVisibleKind;
    }


    public String getMessagevisiblekind() {
        return messageVisibleKind;
    }

    public void setMessagevisiblekind(String messageVisibleKind) {
        this.messageVisibleKind = messageVisibleKind;
    }

    public di_DocumentRoot getDi_documentroot() {
        return di_documentroot;
    }

    public void setDi_documentroot(di_DocumentRoot di_documentroot) {
        this.di_documentroot = di_documentroot;
    }

}