





import java.util.List;
import java.util.ArrayList;

public class filetree_User  {

    private String rootDir;
    private String userId;
    private String pin;
    private String password;





    private filetree_FileTree filetree_filetree;


    public filetree_User(
        String rootDir,        String userId,        String pin,        String password    ) {
        this.rootDir = rootDir;
        this.userId = userId;
        this.pin = pin;
        this.password = password;
    }


    public String getRootdir() {
        return rootDir;
    }

    public void setRootdir(String rootDir) {
        this.rootDir = rootDir;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getPin() {
        return pin;
    }

    public void setPin(String pin) {
        this.pin = pin;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public filetree_FileTree getFiletree_filetree() {
        return filetree_filetree;
    }

    public void setFiletree_filetree(filetree_FileTree filetree_filetree) {
        this.filetree_filetree = filetree_filetree;
    }

}