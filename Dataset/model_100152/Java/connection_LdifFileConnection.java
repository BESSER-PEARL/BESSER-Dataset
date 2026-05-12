





import java.util.List;
import java.util.ArrayList;

public class connection_LdifFileConnection extends Connection {

    private boolean UseLimit;
    private int LimitEntry;
    private String Server;
    private String FilePath;
    private String value;



    public connection_LdifFileConnection(
        boolean UseLimit,        int LimitEntry,        String Server,        String FilePath,        String value    ) {
        super(
        );
        this.UseLimit = UseLimit;
        this.LimitEntry = LimitEntry;
        this.Server = Server;
        this.FilePath = FilePath;
        this.value = value;
    }


    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public int getLimitentry() {
        return LimitEntry;
    }

    public void setLimitentry(int LimitEntry) {
        this.LimitEntry = LimitEntry;
    }
    public String getServer() {
        return Server;
    }

    public void setServer(String Server) {
        this.Server = Server;
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


}