





import java.util.List;
import java.util.ArrayList;

public class Requirement  {

    private String user_id;
    private String requirement_type;
    private String req_description;
    private String requirement_location;





    private List<Reg_User> reg_users;


    public Requirement(
        String user_id,        String requirement_type,        String req_description,        String requirement_location    ) {
        this.user_id = user_id;
        this.requirement_type = requirement_type;
        this.req_description = req_description;
        this.requirement_location = requirement_location;
        this.reg_users = new ArrayList<>();
    }

    public Requirement(
        String user_id,        String requirement_type,        String req_description,        String requirement_location        ArrayList<Reg_User> reg_users    ) {
        this.user_id = user_id;
        this.requirement_type = requirement_type;
        this.req_description = req_description;
        this.requirement_location = requirement_location;
        this.reg_users = reg_users;
    }

    public String getUser_id() {
        return user_id;
    }

    public void setUser_id(String user_id) {
        this.user_id = user_id;
    }
    public String getRequirement_type() {
        return requirement_type;
    }

    public void setRequirement_type(String requirement_type) {
        this.requirement_type = requirement_type;
    }
    public String getReq_description() {
        return req_description;
    }

    public void setReq_description(String req_description) {
        this.req_description = req_description;
    }
    public String getRequirement_location() {
        return requirement_location;
    }

    public void setRequirement_location(String requirement_location) {
        this.requirement_location = requirement_location;
    }

    public List<Reg_User> getReg_users() {
        return reg_users;
    }

    public void addReg_user(Reg_user reg_user) {
        this.reg_users.add(reg_user);
    }

}