





import java.util.List;
import java.util.ArrayList;

public class REFUND_MESSAGES  {

    private String message;
    private String created_at;
    private String _id;
    private String userId;
    private String attach;





    private REFUND refund;


    public REFUND_MESSAGES(
        String message,        String created_at,        String _id,        String userId,        String attach    ) {
        this.message = message;
        this.created_at = created_at;
        this._id = _id;
        this.userId = userId;
        this.attach = attach;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getCreated_at() {
        return created_at;
    }

    public void setCreated_at(String created_at) {
        this.created_at = created_at;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getAttach() {
        return attach;
    }

    public void setAttach(String attach) {
        this.attach = attach;
    }

    public REFUND getRefund() {
        return refund;
    }

    public void setRefund(REFUND refund) {
        this.refund = refund;
    }

}