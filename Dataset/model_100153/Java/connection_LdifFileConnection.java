





import java.util.List;
import java.util.ArrayList;

public class connection_LdifFileConnection extends Connection {

    private int LimitEntry;
    private String FilePath;
    private boolean UseLimit;
    private String Server;
    private String value;



    public connection_LdifFileConnection(
        int LimitEntry,        String FilePath,        boolean UseLimit,        String Server,        String value    ) {
        super(
        );
        this.LimitEntry = LimitEntry;
        this.FilePath = FilePath;
        this.UseLimit = UseLimit;
        this.Server = Server;
        this.value = value;
    }


    public int getLimitentry() {
        return LimitEntry;
    }

    public void setLimitentry(int LimitEntry) {
        this.LimitEntry = LimitEntry;
    }
    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }
    public String getServer() {
        return Server;
    }

    public void setServer(String Server) {
        this.Server = Server;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}