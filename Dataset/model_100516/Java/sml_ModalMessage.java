





import java.util.List;
import java.util.ArrayList;

public class sml_ModalMessage extends InteractionFragment {

    private boolean strict;
    private boolean requested;





    private sml_Role sml_role;




    private sml_Role sml_role;




    private sml_SmlETypedElement sml_smletypedelement;


    public sml_ModalMessage(
        boolean strict,        boolean requested    ) {
        super(
        );
        this.strict = strict;
        this.requested = requested;
    }


    public boolean getStrict() {
        return strict;
    }

    public void setStrict(boolean strict) {
        this.strict = strict;
    }
    public boolean getRequested() {
        return requested;
    }

    public void setRequested(boolean requested) {
        this.requested = requested;
    }

    public sml_Role getSml_role() {
        return sml_role;
    }

    public void setSml_role(sml_Role sml_role) {
        this.sml_role = sml_role;
    }
    public sml_Role getSml_role() {
        return sml_role;
    }

    public void setSml_role(sml_Role sml_role) {
        this.sml_role = sml_role;
    }
    public sml_SmlETypedElement getSml_smletypedelement() {
        return sml_smletypedelement;
    }

    public void setSml_smletypedelement(sml_SmlETypedElement sml_smletypedelement) {
        this.sml_smletypedelement = sml_smletypedelement;
    }

}