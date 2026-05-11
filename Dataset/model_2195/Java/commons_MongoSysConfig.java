





import java.util.List;
import java.util.ArrayList;

public class commons_MongoSysConfig  {

    private String mongoUri;



    public commons_MongoSysConfig(
        String mongoUri    ) {
        this.mongoUri = mongoUri;
    }


    public String getMongouri() {
        return mongoUri;
    }

    public void setMongouri(String mongoUri) {
        this.mongoUri = mongoUri;
    }


}