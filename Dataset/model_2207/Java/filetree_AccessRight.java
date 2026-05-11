





import java.util.List;
import java.util.ArrayList;

public class filetree_AccessRight  {

    private boolean writePermission;
    private boolean readPermission;
    private String userId;





    private filetree_FileTreeElement filetree_filetreeelement;


    public filetree_AccessRight(
        boolean writePermission,        boolean readPermission,        String userId    ) {
        this.writePermission = writePermission;
        this.readPermission = readPermission;
        this.userId = userId;
    }


    public boolean getWritepermission() {
        return writePermission;
    }

    public void setWritepermission(boolean writePermission) {
        this.writePermission = writePermission;
    }
    public boolean getReadpermission() {
        return readPermission;
    }

    public void setReadpermission(boolean readPermission) {
        this.readPermission = readPermission;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }

    public filetree_FileTreeElement getFiletree_filetreeelement() {
        return filetree_filetreeelement;
    }

    public void setFiletree_filetreeelement(filetree_FileTreeElement filetree_filetreeelement) {
        this.filetree_filetreeelement = filetree_filetreeelement;
    }

}