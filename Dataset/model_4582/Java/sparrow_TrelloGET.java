





import java.util.List;
import java.util.ArrayList;

public class sparrow_TrelloGET extends Action {

    private String key;
    private String target;
    private String authtoken;
    private String useraccount;
    private String board;
    private String value;



    public sparrow_TrelloGET(
        String key,        String target,        String authtoken,        String useraccount,        String board,        String value    ) {
        super(
        );
        this.key = key;
        this.target = target;
        this.authtoken = authtoken;
        this.useraccount = useraccount;
        this.board = board;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getAuthtoken() {
        return authtoken;
    }

    public void setAuthtoken(String authtoken) {
        this.authtoken = authtoken;
    }
    public String getUseraccount() {
        return useraccount;
    }

    public void setUseraccount(String useraccount) {
        this.useraccount = useraccount;
    }
    public String getBoard() {
        return board;
    }

    public void setBoard(String board) {
        this.board = board;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}