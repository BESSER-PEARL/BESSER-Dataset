





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_Database  {

    private String author;
    private String collation;
    private String serverAddr;



    public SimpleRDBMS_Database(
        String author,        String collation,        String serverAddr    ) {
        this.author = author;
        this.collation = collation;
        this.serverAddr = serverAddr;
    }


    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getCollation() {
        return collation;
    }

    public void setCollation(String collation) {
        this.collation = collation;
    }
    public String getServeraddr() {
        return serverAddr;
    }

    public void setServeraddr(String serverAddr) {
        this.serverAddr = serverAddr;
    }


}