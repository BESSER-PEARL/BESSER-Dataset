





import java.util.List;
import java.util.ArrayList;

public class db_config_SFTPInfo  {

    private String sftpUser;
    private String sftpPassword;
    private int sftpPort;



    public db_config_SFTPInfo(
        String sftpUser,        String sftpPassword,        int sftpPort    ) {
        this.sftpUser = sftpUser;
        this.sftpPassword = sftpPassword;
        this.sftpPort = sftpPort;
    }


    public String getSftpuser() {
        return sftpUser;
    }

    public void setSftpuser(String sftpUser) {
        this.sftpUser = sftpUser;
    }
    public String getSftppassword() {
        return sftpPassword;
    }

    public void setSftppassword(String sftpPassword) {
        this.sftpPassword = sftpPassword;
    }
    public int getSftpport() {
        return sftpPort;
    }

    public void setSftpport(int sftpPort) {
        this.sftpPort = sftpPort;
    }


}