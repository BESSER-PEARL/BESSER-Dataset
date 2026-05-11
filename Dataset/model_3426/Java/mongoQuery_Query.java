





import java.util.List;
import java.util.ArrayList;

public class mongoQuery_Query  {

    private String key;
    private String stringValue;
    private float numberValue;
    private int integerValue;





    private mongoQuery_Query mongoquery_query;




    private mongoQuery_Selector mongoquery_selector;




    private mongoQuery_Query mongoquery_query;


    public mongoQuery_Query(
        String key,        String stringValue,        float numberValue,        int integerValue    ) {
        this.key = key;
        this.stringValue = stringValue;
        this.numberValue = numberValue;
        this.integerValue = integerValue;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getStringvalue() {
        return stringValue;
    }

    public void setStringvalue(String stringValue) {
        this.stringValue = stringValue;
    }
    public float getNumbervalue() {
        return numberValue;
    }

    public void setNumbervalue(float numberValue) {
        this.numberValue = numberValue;
    }
    public int getIntegervalue() {
        return integerValue;
    }

    public void setIntegervalue(int integerValue) {
        this.integerValue = integerValue;
    }

    public mongoQuery_Query getMongoquery_query() {
        return mongoquery_query;
    }

    public void setMongoquery_query(mongoQuery_Query mongoquery_query) {
        this.mongoquery_query = mongoquery_query;
    }
    public mongoQuery_Selector getMongoquery_selector() {
        return mongoquery_selector;
    }

    public void setMongoquery_selector(mongoQuery_Selector mongoquery_selector) {
        this.mongoquery_selector = mongoquery_selector;
    }
    public mongoQuery_Query getMongoquery_query() {
        return mongoquery_query;
    }

    public void setMongoquery_query(mongoQuery_Query mongoquery_query) {
        this.mongoquery_query = mongoquery_query;
    }

}