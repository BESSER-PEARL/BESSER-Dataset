





import java.util.List;
import java.util.ArrayList;

public class dsl_TrelloPUT extends Action {

    private String authtoken;
    private String list;
    private String source;
    private String value;
    private String useraccount;
    private String key;



    public dsl_TrelloPUT(
        String authtoken,        String list,        String source,        String value,        String useraccount,        String key    ) {
        super(
        );
        this.authtoken = authtoken;
        this.list = list;
        this.source = source;
        this.value = value;
        this.useraccount = useraccount;
        this.key = key;
    }


    public String getAuthtoken() {
        return authtoken;
    }

    public void setAuthtoken(String authtoken) {
        this.authtoken = authtoken;
    }
    public String getList() {
        return list;
    }

    public void setList(String list) {
        this.list = list;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getUseraccount() {
        return useraccount;
    }

    public void setUseraccount(String useraccount) {
        this.useraccount = useraccount;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }


}