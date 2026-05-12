





import java.util.List;
import java.util.ArrayList;

public class Request  {

    private String request_type;
    private int request_id;
    private String requser_id;
    private String request_details;





    private User user;


    public Request(
        String request_type,        int request_id,        String requser_id,        String request_details    ) {
        this.request_type = request_type;
        this.request_id = request_id;
        this.requser_id = requser_id;
        this.request_details = request_details;
    }


    public String getRequest_type() {
        return request_type;
    }

    public void setRequest_type(String request_type) {
        this.request_type = request_type;
    }
    public int getRequest_id() {
        return request_id;
    }

    public void setRequest_id(int request_id) {
        this.request_id = request_id;
    }
    public String getRequser_id() {
        return requser_id;
    }

    public void setRequser_id(String requser_id) {
        this.requser_id = requser_id;
    }
    public String getRequest_details() {
        return request_details;
    }

    public void setRequest_details(String request_details) {
        this.request_details = request_details;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}