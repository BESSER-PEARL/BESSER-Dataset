





import java.util.List;
import java.util.ArrayList;

public class sparrow_TrelloPUT extends Action {

    private String source;
    private String useraccount;
    private String key;
    private String list;
    private String authtoken;
    private String value;



    public sparrow_TrelloPUT(
        String source,        String useraccount,        String key,        String list,        String authtoken,        String value    ) {
        super(
        );
        this.source = source;
        this.useraccount = useraccount;
        this.key = key;
        this.list = list;
        this.authtoken = authtoken;
        this.value = value;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
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
    public String getList() {
        return list;
    }

    public void setList(String list) {
        this.list = list;
    }
    public String getAuthtoken() {
        return authtoken;
    }

    public void setAuthtoken(String authtoken) {
        this.authtoken = authtoken;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}