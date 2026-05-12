





import java.util.List;
import java.util.ArrayList;

public class connection_LdifFileConnection extends Connection {

    private String Server;
    private String value;
    private String FilePath;
    private int LimitEntry;
    private boolean UseLimit;



    public connection_LdifFileConnection(
        String Server,        String value,        String FilePath,        int LimitEntry,        boolean UseLimit    ) {
        super(
        );
        this.Server = Server;
        this.value = value;
        this.FilePath = FilePath;
        this.LimitEntry = LimitEntry;
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
    public String getFilepath() {
        return FilePath;
    }

    public void setFilepath(String FilePath) {
        this.FilePath = FilePath;
    }
    public int getLimitentry() {
        return LimitEntry;
    }

    public void setLimitentry(int LimitEntry) {
        this.LimitEntry = LimitEntry;
    }
    public boolean getUselimit() {
        return UseLimit;
    }

    public void setUselimit(boolean UseLimit) {
        this.UseLimit = UseLimit;
    }


}