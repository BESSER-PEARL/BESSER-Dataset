





import java.util.List;
import java.util.ArrayList;

public class AntScripts_Target extends NamedElement, DescribableElement, CommentableElement {

    private String unless;
    private String if_;



    public AntScripts_Target(
        String unless,        String if_    ) {
        super(
        );
        this.unless = unless;
        this.if_ = if_;
    }


    public String getUnless() {
        return unless;
    }

    public void setUnless(String unless) {
        this.unless = unless;
    }
    public String getIf_() {
        return if_;
    }

    public void setIf_(String if_) {
        this.if_ = if_;
    }


}