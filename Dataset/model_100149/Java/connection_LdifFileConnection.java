





import java.util.List;
import java.util.ArrayList;

public class connection_LdifFileConnection extends Connection {

    private String value;
    private String FilePath;
    private boolean UseLimit;
    private int LimitEntry;
    private String Server;



    public connection_LdifFileConnection(
        String value,        String FilePath,        boolean UseLimit,        int LimitEntry,        String Server    ) {
        super(
        );
        this.value = value;
        this.FilePath = FilePath;
        this.UseLimit = UseLimit;
        this.LimitEntry = LimitEntry;
        this.Server = Server;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
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


}