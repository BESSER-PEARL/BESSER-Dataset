





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_DataLinkDataType extends PredefinedDataType {

    private String readPermission;
    private String integrityControl;
    private String linkControl;
    private String unlink;
    private int length;
    private String writePermission;
    private boolean recovery;



    public sqlmodel_datatypes_DataLinkDataType(
        String readPermission,        String integrityControl,        String linkControl,        String unlink,        int length,        String writePermission,        boolean recovery    ) {
        super(
        );
        this.readPermission = readPermission;
        this.integrityControl = integrityControl;
        this.linkControl = linkControl;
        this.unlink = unlink;
        this.length = length;
        this.writePermission = writePermission;
        this.recovery = recovery;
    }


    public String getReadpermission() {
        return readPermission;
    }

    public void setReadpermission(String readPermission) {
        this.readPermission = readPermission;
    }
    public String getIntegritycontrol() {
        return integrityControl;
    }

    public void setIntegritycontrol(String integrityControl) {
        this.integrityControl = integrityControl;
    }
    public String getLinkcontrol() {
        return linkControl;
    }

    public void setLinkcontrol(String linkControl) {
        this.linkControl = linkControl;
    }
    public String getUnlink() {
        return unlink;
    }

    public void setUnlink(String unlink) {
        this.unlink = unlink;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public String getWritepermission() {
        return writePermission;
    }

    public void setWritepermission(String writePermission) {
        this.writePermission = writePermission;
    }
    public boolean getRecovery() {
        return recovery;
    }

    public void setRecovery(boolean recovery) {
        this.recovery = recovery;
    }


}