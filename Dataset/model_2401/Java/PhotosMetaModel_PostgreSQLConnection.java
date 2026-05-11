





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_PostgreSQLConnection extends Connection {

    private String url;
    private int port;
    private String password;
    private String username;



    public PhotosMetaModel_PostgreSQLConnection(
        String url,        int port,        String password,        String username    ) {
        super(
        );
        this.url = url;
        this.port = port;
        this.password = password;
        this.username = username;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}