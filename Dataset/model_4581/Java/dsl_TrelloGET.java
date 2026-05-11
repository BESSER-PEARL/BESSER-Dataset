





import java.util.List;
import java.util.ArrayList;

public class dsl_TrelloGET extends Action {

    private String value;
    private String target;
    private String key;
    private String useraccount;
    private String authtoken;
    private String board;



    public dsl_TrelloGET(
        String value,        String target,        String key,        String useraccount,        String authtoken,        String board    ) {
        super(
        );
        this.value = value;
        this.target = target;
        this.key = key;
        this.useraccount = useraccount;
        this.authtoken = authtoken;
        this.board = board;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getUseraccount() {
        return useraccount;
    }

    public void setUseraccount(String useraccount) {
        this.useraccount = useraccount;
    }
    public String getAuthtoken() {
        return authtoken;
    }

    public void setAuthtoken(String authtoken) {
        this.authtoken = authtoken;
    }
    public String getBoard() {
        return board;
    }

    public void setBoard(String board) {
        this.board = board;
    }


}