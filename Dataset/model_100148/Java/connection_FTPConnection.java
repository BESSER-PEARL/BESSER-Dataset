





import java.util.List;
import java.util.ArrayList;

public class connection_FTPConnection extends Connection {

    private String Proxyuser;
    private String Mode;
    private String Proxypassword;
    private String KeystorePassword;
    private boolean FTPS;
    private String Proxyport;
    private String CustomEncode;
    private String Method;
    private String KeystoreFile;
    private boolean Usesocks;
    private boolean SFTP;
    private String Username;
    private String Port;
    private String Ecoding;
    private String Host;
    private String Proxyhost;
    private String Password;



    public connection_FTPConnection(
        String Proxyuser,        String Mode,        String Proxypassword,        String KeystorePassword,        boolean FTPS,        String Proxyport,        String CustomEncode,        String Method,        String KeystoreFile,        boolean Usesocks,        boolean SFTP,        String Username,        String Port,        String Ecoding,        String Host,        String Proxyhost,        String Password    ) {
        super(
        );
        this.Proxyuser = Proxyuser;
        this.Mode = Mode;
        this.Proxypassword = Proxypassword;
        this.KeystorePassword = KeystorePassword;
        this.FTPS = FTPS;
        this.Proxyport = Proxyport;
        this.CustomEncode = CustomEncode;
        this.Method = Method;
        this.KeystoreFile = KeystoreFile;
        this.Usesocks = Usesocks;
        this.SFTP = SFTP;
        this.Username = Username;
        this.Port = Port;
        this.Ecoding = Ecoding;
        this.Host = Host;
        this.Proxyhost = Proxyhost;
        this.Password = Password;
    }


    public String getProxyuser() {
        return Proxyuser;
    }

    public void setProxyuser(String Proxyuser) {
        this.Proxyuser = Proxyuser;
    }
    public String getMode() {
        return Mode;
    }

    public void setMode(String Mode) {
        this.Mode = Mode;
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
    public boolean getFtps() {
        return FTPS;
    }

    public void setFtps(boolean FTPS) {
        this.FTPS = FTPS;
    }
    public String getProxyport() {
        return Proxyport;
    }

    public void setProxyport(String Proxyport) {
        this.Proxyport = Proxyport;
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
    public boolean getUsesocks() {
        return Usesocks;
    }

    public void setUsesocks(boolean Usesocks) {
        this.Usesocks = Usesocks;
    }
    public boolean getSftp() {
        return SFTP;
    }

    public void setSftp(boolean SFTP) {
        this.SFTP = SFTP;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
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
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public String getProxyhost() {
        return Proxyhost;
    }

    public void setProxyhost(String Proxyhost) {
        this.Proxyhost = Proxyhost;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }


}