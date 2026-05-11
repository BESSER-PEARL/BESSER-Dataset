





import java.util.List;
import java.util.ArrayList;

public class sparrow_GooglecalPUT extends Action {

    private String value;
    private String key;
    private String authstore;
    private String useraccount;
    private String source;



    public sparrow_GooglecalPUT(
        String value,        String key,        String authstore,        String useraccount,        String source    ) {
        super(
        );
        this.value = value;
        this.key = key;
        this.authstore = authstore;
        this.useraccount = useraccount;
        this.source = source;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getAuthstore() {
        return authstore;
    }

    public void setAuthstore(String authstore) {
        this.authstore = authstore;
    }
    public String getUseraccount() {
        return useraccount;
    }

    public void setUseraccount(String useraccount) {
        this.useraccount = useraccount;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }


}