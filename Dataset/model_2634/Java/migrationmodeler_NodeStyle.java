





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_NodeStyle extends LabelStyle, BorderedStyle {

    private boolean hideLabelByDefault;
    private String labelPosition;





    private migrationmodeler_AbstractNodeRepresentation migrationmodeler_abstractnoderepresentation;


    public migrationmodeler_NodeStyle(
        boolean hideLabelByDefault,        String labelPosition    ) {
        super(
        );
        this.hideLabelByDefault = hideLabelByDefault;
        this.labelPosition = labelPosition;
    }


    public boolean getHidelabelbydefault() {
        return hideLabelByDefault;
    }

    public void setHidelabelbydefault(boolean hideLabelByDefault) {
        this.hideLabelByDefault = hideLabelByDefault;
    }
    public String getLabelposition() {
        return labelPosition;
    }

    public void setLabelposition(String labelPosition) {
        this.labelPosition = labelPosition;
    }

    public migrationmodeler_AbstractNodeRepresentation getMigrationmodeler_abstractnoderepresentation() {
        return migrationmodeler_abstractnoderepresentation;
    }

    public void setMigrationmodeler_abstractnoderepresentation(migrationmodeler_AbstractNodeRepresentation migrationmodeler_abstractnoderepresentation) {
        this.migrationmodeler_abstractnoderepresentation = migrationmodeler_abstractnoderepresentation;
    }

}