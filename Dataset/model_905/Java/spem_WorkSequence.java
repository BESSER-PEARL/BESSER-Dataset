





import java.util.List;
import java.util.ArrayList;

public class spem_WorkSequence extends BreakdownElement {

    private String linkKind;



    public spem_WorkSequence(
        String linkKind    ) {
        super(
        );
        this.linkKind = linkKind;
    }


    public String getLinkkind() {
        return linkKind;
    }

    public void setLinkkind(String linkKind) {
        this.linkKind = linkKind;
    }


}