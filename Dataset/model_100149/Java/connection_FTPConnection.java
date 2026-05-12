





import java.util.List;
import java.util.ArrayList;

public class connection_FTPConnection extends Connection {

    private String Method;
    private String Password;
    private boolean FTPS;
    private boolean Usesocks;
    private String Port;
    private String Proxyhost;
    private String Proxyuser;
    private String Passphrase;
    private String Host;
    private boolean SFTP;
    private String Proxypassword;
    private String Mode;
    private String Privatekey;
    private String CustomEncode;
    private String Username;
    private String KeystorePassword;
    private String Proxyport;
    private String KeystoreFile;
    private String Ecoding;



    public connection_FTPConnection(
        String Method,        String Password,        boolean FTPS,        boolean Usesocks,        String Port,        String Proxyhost,        String Proxyuser,        String Passphrase,        String Host,        boolean SFTP,        String Proxypassword,        String Mode,        String Privatekey,        String CustomEncode,        String Username,        String KeystorePassword,        String Proxyport,        String KeystoreFile,        String Ecoding    ) {
        super(
        );
        this.Method = Method;
        this.Password = Password;
        this.FTPS = FTPS;
        this.Usesocks = Usesocks;
        this.Port = Port;
        this.Proxyhost = Proxyhost;
        this.Proxyuser = Proxyuser;
        this.Passphrase = Passphrase;
        this.Host = Host;
        this.SFTP = SFTP;
        this.Proxypassword = Proxypassword;
        this.Mode = Mode;
        this.Privatekey = Privatekey;
        this.CustomEncode = CustomEncode;
        this.Username = Username;
        this.KeystorePassword = KeystorePassword;
        this.Proxyport = Proxyport;
        this.KeystoreFile = KeystoreFile;
        this.Ecoding = Ecoding;
    }


    public String getMethod() {
        return Method;
    }

    public void setMethod(String Method) {
        this.Method = Method;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public boolean getFtps() {
        return FTPS;
    }

    public void setFtps(boolean FTPS) {
        this.FTPS = FTPS;
    }
    public boolean getUsesocks() {
        return Usesocks;
    }

    public void setUsesocks(boolean Usesocks) {
        this.Usesocks = Usesocks;
    }
    public String getPort() {
        return Port;
    }

    public void setPort(String Port) {
        this.Port = Port;
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
    public String getPassphrase() {
        return Passphrase;
    }

    public void setPassphrase(String Passphrase) {
        this.Passphrase = Passphrase;
    }
    public String getHost() {
        return Host;
    }

    public void setHost(String Host) {
        this.Host = Host;
    }
    public boolean getSftp() {
        return SFTP;
    }

    public void setSftp(boolean SFTP) {
        this.SFTP = SFTP;
    }
    public String getProxypassword() {
        return Proxypassword;
    }

    public void setProxypassword(String Proxypassword) {
        this.Proxypassword = Proxypassword;
    }
    public String getMode() {
        return Mode;
    }

    public void setMode(String Mode) {
        this.Mode = Mode;
    }
    public String getPrivatekey() {
        return Privatekey;
    }

    public void setPrivatekey(String Privatekey) {
        this.Privatekey = Privatekey;
    }
    public String getCustomencode() {
        return CustomEncode;
    }

    public void setCustomencode(String CustomEncode) {
        this.CustomEncode = CustomEncode;
    }
    public String getUsername() {
        return Username;
    }

    public void setUsername(String Username) {
        this.Username = Username;
    }
    public String getKeystorepassword() {
        return KeystorePassword;
    }

    public void setKeystorepassword(String KeystorePassword) {
        this.KeystorePassword = KeystorePassword;
    }
    public String getProxyport() {
        return Proxyport;
    }

    public void setProxyport(String Proxyport) {
        this.Proxyport = Proxyport;
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


}