





import java.util.List;
import java.util.ArrayList;

public class connection_LdifFileConnection extends Connection {

    private String Server;
    private boolean UseLimit;
    private String FilePath;
    private String value;
    private int LimitEntry;



    public connection_LdifFileConnection(
        String Server,        boolean UseLimit,        String FilePath,        String value,        int LimitEntry    ) {
        super(
        );
        this.Server = Server;
        this.UseLimit = UseLimit;
        this.FilePath = FilePath;
        this.value = value;
        this.LimitEntry = LimitEntry;
    }


    public String getServer() {
        return Server;
    }

    public void setServer(String Server) {
        this.Server = Server;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public int getLimitentry() {
        return LimitEntry;
    }

    public void setLimitentry(int LimitEntry) {
        this.LimitEntry = LimitEntry;
    }


}