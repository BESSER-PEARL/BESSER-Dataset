





import java.util.List;
import java.util.ArrayList;

public class db_config_SFTPInfo  {

    private String sftpUser;
    private int sftpPort;
    private String sftpPassword;



    public db_config_SFTPInfo(
        String sftpUser,        int sftpPort,        String sftpPassword    ) {
        this.sftpUser = sftpUser;
        this.sftpPort = sftpPort;
        this.sftpPassword = sftpPassword;
    }


    public String getSftpuser() {
        return sftpUser;
    }

    public void setSftpuser(String sftpUser) {
        this.sftpUser = sftpUser;
    }
    public int getSftpport() {
        return sftpPort;
    }

    public void setSftpport(int sftpPort) {
        this.sftpPort = sftpPort;
    }
    public String getSftppassword() {
        return sftpPassword;
    }

    public void setSftppassword(String sftpPassword) {
        this.sftpPassword = sftpPassword;
    }


}