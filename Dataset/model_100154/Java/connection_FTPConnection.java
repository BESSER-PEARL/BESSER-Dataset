





import java.util.List;
import java.util.ArrayList;

public class connection_FTPConnection extends Connection {

    private String Proxyhost;
    private String Proxyuser;
    private String Proxyport;
    private boolean Usesocks;
    private String Username;
    private String KeystoreFile;
    private String Port;
    private String Ecoding;
    private String Method;
    private boolean FTPS;
    private String Proxypassword;
    private String KeystorePassword;
    private String CustomEncode;
    private boolean SFTP;
    private String Mode;
    private String Password;
    private String Host;



    public connection_FTPConnection(
        String Proxyhost,        String Proxyuser,        String Proxyport,        boolean Usesocks,        String Username,        String KeystoreFile,        String Port,        String Ecoding,        String Method,        boolean FTPS,        String Proxypassword,        String KeystorePassword,        String CustomEncode,        boolean SFTP,        String Mode,        String Password,        String Host    ) {
        super(
        );
        this.Proxyhost = Proxyhost;
        this.Proxyuser = Proxyuser;
        this.Proxyport = Proxyport;
        this.Usesocks = Usesocks;
        this.Username = Username;
        this.KeystoreFile = KeystoreFile;
        this.Port = Port;
        this.Ecoding = Ecoding;
        this.Method = Method;
        this.FTPS = FTPS;
        this.Proxypassword = Proxypassword;
        this.KeystorePassword = KeystorePassword;
        this.CustomEncode = CustomEncode;
        this.SFTP = SFTP;
        this.Mode = Mode;
        this.Password = Password;
        this.Host = Host;
    }


    public String getProxyhost() {
        return Proxyhost;
    }

    public void setProxyhost(String Proxyhost) {
        this.Proxyhost = Proxyhost;
    }
    public String getProxyuser() {
        return Proxyuser;
    }

    public void setProxyuser(String Proxyuser) {
        this.Proxyuser = Proxyuser;
    }
    public String getProxyport() {
        return Proxyport;
    }

    public void setProxyport(String Proxyport) {
        this.Proxyport = Proxyport;
    }
    public boolean getUsesocks() {
        return Usesocks;
    }

    public void setUsesocks(boolean Usesocks) {
        this.Usesocks = Usesocks;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getKeystorefile() {
        return KeystoreFile;
    }

    public void setKeystorefile(String KeystoreFile) {
        this.KeystoreFile = KeystoreFile;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public String getEcoding() {
        return Ecoding;
    }

    public void setEcoding(String Ecoding) {
        this.Ecoding = Ecoding;
    }
    public String getMethod() {
        return Method;
    }

    public void setMethod(String Method) {
        this.Method = Method;
    }
    public boolean getFtps() {
        return FTPS;
    }

    public void setFtps(boolean FTPS) {
        this.FTPS = FTPS;
    }
    public String getProxypassword() {
        return Proxypassword;
    }

    public void setProxypassword(String Proxypassword) {
        this.Proxypassword = Proxypassword;
    }
    public String getKeystorepassword() {
        return KeystorePassword;
    }

    public void setKeystorepassword(String KeystorePassword) {
        this.KeystorePassword = KeystorePassword;
    }
    public String getCustomencode() {
        return CustomEncode;
    }

    public void setCustomencode(String CustomEncode) {
        this.CustomEncode = CustomEncode;
    }
    public boolean getSftp() {
        return SFTP;
    }

    public void setSftp(boolean SFTP) {
        this.SFTP = SFTP;
    }
    public String getMode() {
        return Mode;
    }

    public void setMode(String Mode) {
        this.Mode = Mode;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }


}