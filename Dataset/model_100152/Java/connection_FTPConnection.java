





import java.util.List;
import java.util.ArrayList;

public class connection_FTPConnection extends Connection {

    private boolean FTPS;
    private String Host;
    private String Password;
    private boolean SFTP;
    private String KeystorePassword;
    private String Username;
    private String Proxyport;
    private String Proxypassword;
    private String Proxyuser;
    private String CustomEncode;
    private String Method;
    private String KeystoreFile;
    private String Ecoding;
    private String Mode;
    private String Proxyhost;
    private String Port;
    private boolean Usesocks;



    public connection_FTPConnection(
        boolean FTPS,        String Host,        String Password,        boolean SFTP,        String KeystorePassword,        String Username,        String Proxyport,        String Proxypassword,        String Proxyuser,        String CustomEncode,        String Method,        String KeystoreFile,        String Ecoding,        String Mode,        String Proxyhost,        String Port,        boolean Usesocks    ) {
        super(
        );
        this.FTPS = FTPS;
        this.Host = Host;
        this.Password = Password;
        this.SFTP = SFTP;
        this.KeystorePassword = KeystorePassword;
        this.Username = Username;
        this.Proxyport = Proxyport;
        this.Proxypassword = Proxypassword;
        this.Proxyuser = Proxyuser;
        this.CustomEncode = CustomEncode;
        this.Method = Method;
        this.KeystoreFile = KeystoreFile;
        this.Ecoding = Ecoding;
        this.Mode = Mode;
        this.Proxyhost = Proxyhost;
        this.Port = Port;
        this.Usesocks = Usesocks;
    }


    public boolean getFtps() {
        return FTPS;
    }

    public void setFtps(boolean FTPS) {
        this.FTPS = FTPS;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public boolean getSftp() {
        return SFTP;
    }

    public void setSftp(boolean SFTP) {
        this.SFTP = SFTP;
    }
    public String getKeystorepassword() {
        return KeystorePassword;
    }

    public void setKeystorepassword(String KeystorePassword) {
        this.KeystorePassword = KeystorePassword;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getProxyport() {
        return Proxyport;
    }

    public void setProxyport(String Proxyport) {
        this.Proxyport = Proxyport;
    }
    public String getProxypassword() {
        return Proxypassword;
    }

    public void setProxypassword(String Proxypassword) {
        this.Proxypassword = Proxypassword;
    }
    public String getProxyuser() {
        return Proxyuser;
    }

    public void setProxyuser(String Proxyuser) {
        this.Proxyuser = Proxyuser;
    }
    public String getCustomencode() {
        return CustomEncode;
    }

    public void setCustomencode(String CustomEncode) {
        this.CustomEncode = CustomEncode;
    }
    public String getMethod() {
        return Method;
    }

    public void setMethod(String Method) {
        this.Method = Method;
    }
    public String getKeystorefile() {
        return KeystoreFile;
    }

    public void setKeystorefile(String KeystoreFile) {
        this.KeystoreFile = KeystoreFile;
    }
    public String getEcoding() {
        return Ecoding;
    }

    public void setEcoding(String Ecoding) {
        this.Ecoding = Ecoding;
    }
    public String getMode() {
        return Mode;
    }

    public void setMode(String Mode) {
        this.Mode = Mode;
    }
    public String getProxyhost() {
        return Proxyhost;
    }

    public void setProxyhost(String Proxyhost) {
        this.Proxyhost = Proxyhost;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
    }
    public boolean getUsesocks() {
        return Usesocks;
    }

    public void setUsesocks(boolean Usesocks) {
        this.Usesocks = Usesocks;
    }


}